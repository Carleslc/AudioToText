## Example: Spanish to English using DeepL

[**Example Notebook**](https://github.com/Carleslc/AudioToText/blob/master/examples/spanish-to-english-deepl/spanish-to-english-deepl.ipynb)

This example transcribes the audio of a spanish video file (low-res so it can be uploaded fast) using Whisper to its source language in TXT, VTT and SRT formats.

Then uses DeepL API to translate the generated transcripts to english.

## Input

**task**: `Transcribe`

**audio_file**: [`Whisper-Example.3gp`](https://carleslc.me/AudioToText/examples/spanish-to-english-deepl/Whisper-Example.3gp) ([Original YouTube video](https://www.youtube.com/watch?v=JuMEmF-2FsA))

**use_model**: `large-v2`

**language:** `Auto-Detect` (Spanish)

## Output

**output_formats**: `txt,vtt,srt`

[audio_transcription/Whisper-Example.txt](audio_transcription/Whisper-Example.txt)

[audio_transcription/Whisper-Example.vtt](audio_transcription/Whisper-Example.vtt)

[audio_transcription/Whisper-Example.srt](audio_transcription/Whisper-Example.srt)

**deepl_target_language**: `English (British)`

[audio_transcription/Whisper-Example_English (British).txt](audio_transcription/Whisper-Example_English%20(British).txt)

[audio_transcription/Whisper-Example_English (British).vtt](audio_transcription/Whisper-Example_English%20(British).vtt)

[audio_transcription/Whisper-Example_English (British).srt](audio_transcription/Whisper-Example_English%20(British).srt)
