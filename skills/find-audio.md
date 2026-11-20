# Skill: find music and sound effects

Use `scripts/openverse.py` (Openverse API, no key needed; Freesound SFX + Jamendo music).

```bash
. .venv/bin/activate
python3 scripts/openverse.py search "whoosh" --kind sfx --max 10
python3 scripts/openverse.py get "whoosh" --kind sfx --pick 1      # -> assets/sfx/
python3 scripts/openverse.py search "upbeat" --kind music
python3 scripts/openverse.py get "upbeat" --kind music --pick 2    # -> assets/music/
```

- Default license filter is commercial-safe (`cc0,by,pdm`).
- Every download appends attribution to `CREDITS.md` in the target folder. CC-BY tracks must be credited in the video description.
- Prefer CC0 SFX. Preview with `ffprobe`/ffmpeg before using.
