## Example: Chinese to English using DeepL

This example transcribes a chinese audio file using Whisper to its source language in TXT, VTT and SRT.
Then uses DeepL API to translate the results to english.

## Input

**task**: `Transcribe`

**audio_file**: [`chinese.wav`](chinese.wav)

**use_model**: `large-v2`

**language:** `Auto-Detect` (Chinese)

## Output

**output_formats**: `txt,vtt,srt`

[audio_transcription/chinese.txt](audio_transcription/chinese.txt)

[audio_transcription/chinese.vtt](audio_transcription/chinese.vtt)

[audio_transcription/chinese.srt](audio_transcription/chinese.srt)

**deepl_target_language**: `English (British)`

[audio_transcription/chinese_English (British).txt](audio_transcription/chinese_English%20(British).txt)

[audio_transcription/chinese_English (British).vtt](audio_transcription/chinese_English%20(British).vtt)

[audio_transcription/chinese_English (British).srt](audio_transcription/chinese_English%20(British).srt)
