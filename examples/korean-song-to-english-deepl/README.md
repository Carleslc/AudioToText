## Example: K-pop

This example transcribes a korean song file using Whisper to its source language in TXT, VTT, SRT, TSV and JSON formats.

Then uses DeepL API to translate the generated transcripts to english.

## Input

**task**: `Transcribe`

**audio_file**: [`kpop.wav`](https://carleslc.me/AudioToText/examples/korean-song-to-english-deepl/kpop.wav)

**use_model**: `small`

**language:** `Auto-Detect` (Korean)

## Output

**output_formats**: `txt,vtt,srt,tsv,json`

[audio_transcription/kpop.txt](audio_transcription/kpop.txt)

[audio_transcription/kpop.vtt](audio_transcription/kpop.vtt)

[audio_transcription/kpop.srt](audio_transcription/kpop.srt)

[audio_transcription/kpop.tsv](audio_transcription/kpop.tsv)

[audio_transcription/kpop.json](audio_transcription/kpop.json)

**deepl_target_language**: `English (American)`

**deepl_coherence_preference**: `Translate each line independently`

[audio_transcription/kpop_English (American).txt](audio_transcription/kpop_English%20(American).txt)

[audio_transcription/kpop_English (American).vtt](audio_transcription/kpop_English%20(American).vtt)

[audio_transcription/kpop_English (American).srt](audio_transcription/kpop_English%20(American).srt)

[audio_transcription/kpop_English (American).tsv](audio_transcription/kpop_English%20(American).tsv)

[audio_transcription/kpop_English (American).json](audio_transcription/kpop_English%20(American).json)
