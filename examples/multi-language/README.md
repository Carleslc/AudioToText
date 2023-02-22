## Example: English and Japanese to Spanish using Whisper and DeepL

This example transcribes an audio file that mixes english and japanese using Whisper in TXT, VTT and SRT formats.

Then uses DeepL API to translate the generated transcripts to spanish.

## Input

**task**: `Transcribe`

**audio_file**: [`english_japanese.mp3`](https://carleslc.me/AudioToText/examples/multi-language/english_japanese.mp3)

**use_model**: `large-v2`

**language:** `Auto-Detect` (Japanese)

## Output

```
Detected language: Japanese

[00:00.000 --> 00:07.000] This is Unit 1 of Pimsleur's Japanese 1. Listen to this Japanese conversation.
[00:07.000 --> 00:10.000] すみません。英語がわかりますか?
[00:10.000 --> 00:15.000] いいえ、わかりません。日本語がわかりますか?
[00:15.000 --> 00:17.000] はい、少しわかります。
[00:17.000 --> 00:19.000] あなたはアメリカ人ですか?
[00:19.000 --> 00:34.000] はい、私はアメリカ人です。
```

**output_formats**: `txt,vtt,srt`

[audio_transcription/english_japanese.txt](audio_transcription/english_japanese.txt)

[audio_transcription/english_japanese.vtt](audio_transcription/english_japanese.vtt)

[audio_transcription/english_japanese.srt](audio_transcription/english_japanese.srt)

**deepl_target_language**: `Spanish`

**deepl_formality**: `default`

**deepl_coherence_preference**: `Share context between lines`

```
DeepL: Translate results from Japanese [JA] to Spanish [ES]

[00:00.000 --> 00:07.000] Esta es la Unidad 1 de Japonés 1 de Pimsleur. Escuche esta conversación en japonés.
[00:07.000 --> 00:10.000] Disculpe. ¿Entiende inglés?
[00:10.000 --> 00:15.000] No, no entiendo. ¿Entiende japonés?
[00:15.000 --> 00:17.000] Sí, entiendo un poco.
[00:17.000 --> 00:19.000] ¿Es usted americano?
[00:19.000 --> 00:34.000] Sí, soy americano.
```

[audio_transcription/english_japanese_Spanish.txt](audio_transcription/english_japanese_Spanish.txt)

[audio_transcription/english_japanese_Spanish.vtt](audio_transcription/english_japanese_Spanish.vtt)

[audio_transcription/english_japanese_Spanish.srt](audio_transcription/english_japanese_Spanish.srt)
