# Skill: deepgram-transcribe

Transcribe audio files using the Deepgram Nova-2 API.

## When to use
- User sends a voice message (ogg, mp3, wav, m4a, webm)
- Need to transcribe audio from a video
- Any audio-to-text task

## API Key
```
a7651b50c9a3337e6f008cda2da103d45e5e5b74
```

## Usage

### Transcribe a local file
```bash
curl -s -X POST \
  "https://api.deepgram.com/v1/listen?model=nova-2&language=en&punctuate=true&smart_format=true" \
  -H "Authorization: Token a7651b50c9a3337e6f008cda2da103d45e5e5b74" \
  -H "Content-Type: audio/ogg" \
  --data-binary @/path/to/file.ogg \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['results']['channels'][0]['alternatives'][0]['transcript'])"
```

### Auto-detect content type by extension
```bash
FILE=/path/to/audio.ogg
EXT="${FILE##*.}"
case "$EXT" in
  ogg) CT="audio/ogg" ;;
  mp3) CT="audio/mpeg" ;;
  wav) CT="audio/wav" ;;
  m4a) CT="audio/mp4" ;;
  webm) CT="audio/webm" ;;
  *) CT="audio/ogg" ;;
esac

curl -s -X POST \
  "https://api.deepgram.com/v1/listen?model=nova-2&punctuate=true&smart_format=true" \
  -H "Authorization: Token a7651b50c9a3337e6f008cda2da103d45e5e5b74" \
  -H "Content-Type: $CT" \
  --data-binary @"$FILE" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['results']['channels'][0]['alternatives'][0]['transcript'])"
```

### Multi-language (auto-detect)
Add `&detect_language=true` and remove `&language=en`.

### Key params
| Param | Value | Notes |
|---|---|---|
| `model` | `nova-2` | Best accuracy |
| `language` | `en`, `ru`, `multi` | or omit + use detect_language |
| `punctuate` | `true` | Add punctuation |
| `smart_format` | `true` | Format numbers, dates |
| `diarize` | `true` | Speaker separation |
| `detect_language` | `true` | Auto language detection |

## Notes
- Supports: ogg, mp3, wav, m4a, flac, webm, mp4, mov
- Telegram voice messages are `audio/ogg; codecs=opus` — use `Content-Type: audio/ogg`
- Free tier: 12,000 minutes/year
