## Example: K-pop

This example transcribes a korean song file using Whisper to its source language in TXT, VTT, SRT, TSV and JSON formats.

Then uses DeepL API to translate the generated transcripts to english.

## Input

**task**: `Transcribe`

**audio_file**: [`kpop.wav`](https://carleslc.me/AudioToText/examples/korean-song-to-english-deepl/kpop.wav)

**use_model**: `small`

**language:** `Korean`

## Output

```
[00:01.000 --> 00:05.000]  어둠 많이 나의 전부였던 동안
[00:05.000 --> 00:08.000]  숨이 뻗자도록 달려왔잖아
[00:08.000 --> 00:10.000]  Never say, time's up
[00:10.000 --> 00:12.000]  경계의 끝으로
[00:12.000 --> 00:30.840]  지금 이따가
```

**output_formats**: `txt,vtt,srt,tsv,json`

[audio_transcription/kpop.txt](audio_transcription/kpop.txt)

[audio_transcription/kpop.vtt](audio_transcription/kpop.vtt)

[audio_transcription/kpop.srt](audio_transcription/kpop.srt)

[audio_transcription/kpop.tsv](audio_transcription/kpop.tsv)

[audio_transcription/kpop.json](audio_transcription/kpop.json)

**deepl_target_language**: `English (American)`

**deepl_formality**: `default`

**deepl_coherence_preference**: `Translate each line independently`

```
DeepL: Translate results from Korean [KO] to English (American) [EN-US]

[00:01.000 --> 00:05.000] While the darkness was all I had
[00:05.000 --> 00:08.000] You've been running to catch your breath
[00:08.000 --> 00:10.000] Never say, time's up
[00:10.000 --> 00:12.000] To the end of the boundary
[00:12.000 --> 00:30.840] Now, later

DeepL: Character usage: 62 / 500000 (0.01%)
```

[audio_transcription/kpop_English (American).txt](audio_transcription/kpop_English%20(American).txt)

[audio_transcription/kpop_English (American).vtt](audio_transcription/kpop_English%20(American).vtt)

[audio_transcription/kpop_English (American).srt](audio_transcription/kpop_English%20(American).srt)

[audio_transcription/kpop_English (American).tsv](audio_transcription/kpop_English%20(American).tsv)

[audio_transcription/kpop_English (American).json](audio_transcription/kpop_English%20(American).json)
