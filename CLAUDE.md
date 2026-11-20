# AI Video Editing Workspace

This folder is my workspace for AI-assisted video editing. Claude: read this file first, and use the locations below instead of asking where things are.

## Folder map

| Folder | What lives there |
|---|---|
| `raw-videos/` | Original footage. **Read-only: never edit or overwrite.** |
| `references/` | Scripts, outlines, transcripts, briefs: what a video is *about* |
| `inspirations/` | Example videos/notes showing the *style* I like |
| `brand-kit/` | Logos, colors, intro/outro, brand guidelines |
| `assets/music/` | Background music |
| `assets/sfx/` | Sound effects |
| `assets/images/` | Overlays, icons, stock images |
| `assets/fonts/` | Fonts for captions/titles |
| `skills/` | Reusable editing workflows. Check here before starting a task |
| `projects/` | One sub-folder per video (plans, cut lists, subtitles, drafts) |
| `exports/` | Final rendered videos only |

## Workflow

1. Read the brief/script in `references/` and the style notes in `inspirations/`.
2. Check `skills/` for a matching workflow.
3. Create `projects/<YYYY-MM-DD_name>/` and keep working files there.
4. Pull footage from `raw-videos/`, music/sfx/images/fonts from `assets/`, branding from `brand-kit/`.
5. Render finals to `exports/` as `projectname_platform_vN.mp4`.

## Rules

- Never modify files in `raw-videos/`; work on copies or use non-destructive cuts.
- Always apply the brand kit (colors, fonts, logo) unless told otherwise.
- Don't delete anything without asking.
- Keep the user's original filenames; name new files descriptively.

## Installed tools (how to run them)

Activate Python tools first: `. .venv/bin/activate`. Node tools are in `node_modules/` (`npm install` restores them; the Python venv is rebuilt with `python3 -m venv .venv && pip install yt-dlp openai-whisper`).

| Tool | Use | Command |
|---|---|---|
| FFmpeg / ffprobe | cut, convert, mix audio | `ffmpeg ...` |
| yt-dlp | download reference/inspiration videos | `yt-dlp -o "inspirations/%(title)s.%(ext)s" <url>` |
| Whisper | transcripts + captions | `whisper clip.mp4 --model small --output_format srt` (use `--model tiny` for speed) |
| Remotion | React-based video rendering | `npx remotion render <entry> <comp> out.mp4` |
| Hyperframes | HTML-to-video rendering | `npx hyperframes init <name>` then `npx hyperframes render` |
| Openverse | free SFX/music search + download | see `skills/find-audio.md` |

Cloud-sandbox note: if a render can't find Chrome, set `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium` (Remotion: `--browser-executable`). Only download content you have the rights to use.

## How I like my videos edited

Defaults for every project. Override per project only when I say so. Anything not listed here: ask me.

- **Platforms / formats:** I edit for YouTube (16:9), Shorts/Reels/TikTok (9:16), and Instagram feed (4:5 or 1:1), often repurposing one video for several. Build the master first, then reframe per platform, keeping the speaker and captions inside safe zones.
- **Pacing & cuts:** Fast and punchy. Tight jump cuts, remove silences longer than ~0.3s, cut filler words and flubs, change the visual (cut, zoom, b-roll, overlay) every 2-4 seconds.
- **Captions:** Bold, centered, word-by-word, with the spoken word highlighted. Use the brand font and colors. Generate from Whisper transcripts and proofread names and jargon.
- **Music:** Always add a background track, ducked to about -20 dB under speech. Pick the mood to match the video. Prefer CC0 or properly credited tracks (`skills/find-audio.md`).
- **Sound effects:** Use them frequently: whooshes on transitions, hits on text and graphic pops, subtle risers into key moments. Keep them short and mixed below the voice.
- **Color / look:** Not set yet. Ask, or follow `brand-kit/` and `inspirations/`.
- **Transitions:** Not set yet. Default to hard cuts, with quick whip or zoom transitions on topic changes.
- **Intro / outro:** Not set yet. Use files from `brand-kit/` if present, otherwise skip.
- **Typical length:** Not set yet. Ask per project.
- **Things to avoid:** Not set yet. Until told otherwise: dead air, long static shots, captions that cover the face, music louder than the voice.
