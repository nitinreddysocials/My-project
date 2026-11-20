#!/usr/bin/env python3
"""Search and download free SFX / music from Openverse (no API key needed).

Openverse indexes Freesound (sound effects), Jamendo and others (music), with
license info. Anonymous use is rate limited; set OPENVERSE_TOKEN for more.

Usage:
  scripts/openverse.py search "whoosh" [--kind sfx|music] [--max 10] [--license cc0,by]
  scripts/openverse.py get "whoosh" [--kind sfx|music] [--pick 1] [--out assets/sfx]
"""
import argparse, json, os, re, sys, urllib.parse, urllib.request

API = "https://api.openverse.org/v1/audio/"
# kind -> (openverse category, default sources, default output dir)
KINDS = {"sfx": (None, "freesound", "assets/sfx"),
         "music": ("music", "jamendo,freesound", "assets/music")}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "video-workspace/1.0"})
    tok = os.environ.get("OPENVERSE_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    return urllib.request.urlopen(req, timeout=60)

def search(q, kind, n, lic):
    cat, src, _ = KINDS[kind]
    p = {"q": q, "category": cat, "page_size": n, "license": lic}
    if src: p["source"] = src
    with fetch(API + "?" + urllib.parse.urlencode({k: v for k, v in p.items() if v})) as r:
        return json.load(r)["results"]

def show(res):
    for i, r in enumerate(res, 1):
        d = f'{r["duration"]/1000:.1f}s' if r.get("duration") else "?"
        print(f'{i:>2}. {r["title"][:60]} | {d} | {r["license"].upper()} {r.get("license_version","")} | by {r.get("creator")} | {r["source"]}')

def main():
    a = argparse.ArgumentParser()
    a.add_argument("cmd", choices=["search", "get"]); a.add_argument("query")
    a.add_argument("--kind", choices=KINDS, default="sfx")
    a.add_argument("--max", type=int, default=10); a.add_argument("--pick", type=int, default=1)
    a.add_argument("--license", default="cc0,by,pdm", help="comma list; default is commercial-safe")
    a.add_argument("--out")
    o = a.parse_args()
    res = search(o.query, o.kind, o.max, o.license)
    if not res: sys.exit("No results.")
    if o.cmd == "search": return show(res)
    r = res[o.pick - 1]
    out = o.out or KINDS[o.kind][2]; os.makedirs(out, exist_ok=True)
    ext = os.path.splitext(urllib.parse.urlparse(r["url"]).path)[1].lstrip(".").lower() or "mp3"
    name = re.sub(r"[^\w-]+", "_", r["title"]).strip("_")[:50] or "audio"
    path = os.path.join(out, f"{name}.{ext}")
    with fetch(r["url"]) as resp, open(path, "wb") as f: f.write(resp.read())
    with open(os.path.join(out, "CREDITS.md"), "a") as f:
        f.write(f'- {os.path.basename(path)}: "{r["title"]}" by {r.get("creator")} ({r["license"].upper()} {r.get("license_version","")}) {r.get("foreign_landing_url")}\n')
    print("Saved", path, "|", r["license"].upper(), "| credit logged in", os.path.join(out, "CREDITS.md"))

if __name__ == "__main__": main()
