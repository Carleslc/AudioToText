## Example: English and Japanese to Spanish using Whisper and DeepL

[**Example Notebook**](https://github.com/Carleslc/AudioToText/blob/master/examples/multi-language/multi-language-example.ipynb)

This example transcribes an audio file that mixes english and japanese using Whisper in TXT, VTT and SRT formats.
Then uses DeepL API to translate the results to spanish.

## Input

**task**: `Transcribe`

**audio_file**: [`english_japanese.mp3`](english_japanese.mp3)

**use_model**: `large-v2`

**language:** `Auto-Detect` (Japanese)

## Output

**output_formats**: `txt,vtt,srt`

[audio_transcription/english_japanese.txt](audio_transcription/english_japanese.txt)

[audio_transcription/english_japanese.vtt](audio_transcription/english_japanese.vtt)

[audio_transcription/english_japanese.srt](audio_transcription/english_japanese.srt)

**deepl_target_language**: `Spanish`

[audio_transcription/english_japanese_Spanish.txt](audio_transcription/english_japanese_Spanish.txt)

[audio_transcription/english_japanese_Spanish.vtt](audio_transcription/english_japanese_Spanish.vtt)

[audio_transcription/english_japanese_Spanish.srt](audio_transcription/english_japanese_Spanish.srt)
