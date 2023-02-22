## Example: Chinese to English using DeepL

This example transcribes a chinese audio file using Whisper to its source language in TXT, VTT and SRT formats.

Then uses DeepL API to translate the generated transcripts to english.

## Input

**task**: `Transcribe`

**audio_file**: [`chinese.wav`](https://carleslc.me/AudioToText/examples/chinese-to-english-deepl/chinese.wav)

**use_model**: `large-v2`

**language:** `Auto-Detect` (Chinese)

## Output

```
Detected language: Chinese

[00:00.600 --> 00:04.120] 院子门口不远处就是一个地铁站
[00:04.140 --> 00:06.720] 这是一个美丽而神奇的景象
[00:07.760 --> 00:10.520] 树上长满了又大又甜的桃子
[00:11.520 --> 00:14.600] 海豚和鲸鱼的表演是很好看的节目
[00:14.600 --> 00:19.400] 邮局门前的棱形道上有一个蓝色的邮箱
```

**output_formats**: `txt,vtt,srt`

[audio_transcription/chinese.txt](audio_transcription/chinese.txt)

[audio_transcription/chinese.vtt](audio_transcription/chinese.vtt)

[audio_transcription/chinese.srt](audio_transcription/chinese.srt)

**deepl_target_language**: `English (British)`

**deepl_coherence_preference**: `Share context between lines`

```
DeepL: Translate results from Chinese [ZH] to English (British) [EN-GB]

[00:00.600 --> 00:04.120] There is a tube station not far from the entrance to the yard 
[00:04.140 --> 00:06.720] It is a beautiful and magical sight 
[00:07.760 --> 00:10.520] The trees are full of big, sweet peaches 
[00:11.520 --> 00:14.600] The dolphin and whale shows are great to watch 
[00:14.600 --> 00:19.400] There is a blue mailbox on the ribbed path in front of the post office
```

[audio_transcription/chinese_English (British).txt](audio_transcription/chinese_English%20(British).txt)

[audio_transcription/chinese_English (British).vtt](audio_transcription/chinese_English%20(British).vtt)

[audio_transcription/chinese_English (British).srt](audio_transcription/chinese_English%20(British).srt)
