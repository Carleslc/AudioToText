## Example: Transcribe and Translate multiple files

This example transcribes different audio files in different languages from other examples using Whisper in TXT, VTT and SRT formats.

Then uses DeepL API to translate the generated transcripts to spanish.

## Input

**task**: `Transcribe`

**audio_file**: [`chinese.wav, bruce.mp3, english_japanese.mp3, french.wav`](https://github.com/Carleslc/AudioToText/blob/master/examples/multiple-files/)

**use_model**: `large-v2`

**language:** `Auto-Detect`

## Output

```
GPU 0: Tesla T4 (UUID: GPU-1c00bab7-1e75-192c-33cb-637ef416d04f)

Loading large-v2 model...
Model large-v2 is multilingual and has 1,541,384,960 parameters.

-- TRANSCRIPTION --

Processing: chinese.wav

Detected language: Chinese

[00:00.600 --> 00:04.120] 院子门口不远处就是一个地铁站
[00:04.140 --> 00:06.720] 这是一个美丽而神奇的景象
[00:07.760 --> 00:10.520] 树上长满了又大又甜的桃子
[00:11.520 --> 00:14.600] 海豚和鲸鱼的表演是很好看的节目
[00:14.600 --> 00:19.400] 邮局门前的棱形道上有一个蓝色的邮箱

Processing: bruce.mp3

Detected language: English

[00:00.000 --> 00:03.000]  I get up in the evening
[00:04.000 --> 00:07.000]  And I ain't got nothing to say
[00:07.000 --> 00:09.000]  I come home in the morning
[00:10.000 --> 00:13.000]  I go to bed feeling the same way
[00:13.000 --> 00:16.000]  I ain't nothing but tired
[00:17.000 --> 00:20.000]  Man, I'm just tired and bored with myself
[00:20.000 --> 00:22.000]  Hey there, baby
[00:24.000 --> 00:26.000]  I could use just a little help
[00:26.000 --> 00:29.000]  You can't start a fire
[00:29.000 --> 00:33.000]  You can't start a fire without a spark
[00:33.000 --> 00:35.000]  There's guns for hire
[00:35.000 --> 00:39.000]  Even if we're just dancing in the dark

Processing: english_japanese.mp3

Detected language: Japanese

[00:00.000 --> 00:07.000] This is Unit 1 of Pimsleur's Japanese 1. Listen to this Japanese conversation.
[00:07.000 --> 00:10.000] すみません。英語がわかりますか?
[00:10.000 --> 00:15.000] いいえ、わかりません。日本語がわかりますか?
[00:15.000 --> 00:17.000] はい、少しわかります。
[00:17.000 --> 00:19.000] あなたはアメリカ人ですか?
[00:19.000 --> 00:34.000] はい、私はアメリカ人です。

Processing: french.wav

Detected language: French

[00:00.000 --> 00:06.640]  Whisper est un système de reconnaissance automatique de la parole entraîné sur 680.000
[00:06.640 --> 00:10.720]  heures de données multilingues et multitâches récoltées sur Internet.
[00:10.720 --> 00:16.000]  Nous établissons que l'utilisation de données d'un tel nombre et d'une telle diversité
[00:16.000 --> 00:20.500]  est la raison pour laquelle The System est à même de comprendre de nombreux accents
[00:20.500 --> 00:24.880]  en dépit de bruit de fond, de comprendre un vocabulaire technique et de réussir la
[00:24.880 --> 00:27.640]  traduction depuis diverses langues en anglais.
[00:27.640 --> 00:33.360]  Nous distribuons en tant que logiciel libre le code source pour nos modèles et pour l'inférence
[00:33.360 --> 00:37.040]  afin que ceux-ci puissent servir comme un point de départ pour construire des applications
[00:37.040 --> 00:54.560]  utiles et pour aider à faire progresser la recherche en traitement de la parole.
```

**output_formats**: `txt,vtt,srt`

```
Writing results...

audio_transcription/chinese.txt
audio_transcription/chinese.vtt
audio_transcription/chinese.srt

audio_transcription/bruce.txt
audio_transcription/bruce.vtt
audio_transcription/bruce.srt

audio_transcription/english_japanese.txt
audio_transcription/english_japanese.vtt
audio_transcription/english_japanese.srt

audio_transcription/french.txt
audio_transcription/french.vtt
audio_transcription/french.srt
```

**deepl_target_language**: `Spanish`

**deepl_formality**: `default`

**deepl_coherence_preference**: `Share context between lines`

```
chinese.wav

DeepL: Translate results from Chinese [ZH] to Spanish [ES]

[00:00.600 --> 00:04.120] Hay una estación de metro no muy lejos de la entrada al patio
[00:04.140 --> 00:06.720] Es una vista hermosa y mágica
[00:07.760 --> 00:10.520] Los árboles están llenos de melocotones grandes y dulces
[00:11.520 --> 00:14.600] Los espectáculos de delfines y ballenas son geniales de ver
[00:14.600 --> 00:19.400] Hay un buzón azul en el camino acanalado frente a la oficina de correos

DeepL: Character usage: 78 / 500000 (0.02%)

bruce.mp3

DeepL: Translate results from English [EN] to Spanish [ES]

[00:00.000 --> 00:03.000] Me levanto por la noche
[00:04.000 --> 00:07.000] Y no tengo nada que decir
[00:07.000 --> 00:09.000] Vuelvo a casa por la mañana
[00:10.000 --> 00:13.000] Me acuesto sintiéndome igual
[00:13.000 --> 00:16.000] No estoy más que cansado
[00:17.000 --> 00:20.000] Tío, estoy cansado y aburrido de mí mismo
[00:20.000 --> 00:22.000] Hola, baby
[00:24.000 --> 00:26.000] Me vendría bien un poco de ayuda
[00:26.000 --> 00:29.000] No puedes encender un fuego
[00:29.000 --> 00:33.000] No puedes encender un fuego sin una chispa
[00:33.000 --> 00:35.000] Hay pistolas de alquiler
[00:35.000 --> 00:39.000] Incluso si sólo estamos bailando en la oscuridad

DeepL: Character usage: 441 / 500000 (0.09%)

english_japanese.mp3

DeepL: Translate results from Japanese [JA] to Spanish [ES]

[00:00.000 --> 00:07.000] Esta es la Unidad 1 de Japonés 1 de Pimsleur. Escuche esta conversación en japonés.
[00:07.000 --> 00:10.000] Disculpe. ¿Entiende inglés?
[00:10.000 --> 00:15.000] No, no entiendo. ¿Entiende japonés?
[00:15.000 --> 00:17.000] Sí, entiendo un poco.
[00:17.000 --> 00:19.000] ¿Es usted americano?
[00:19.000 --> 00:34.000] Sí, soy americano.

DeepL: Character usage: 596 / 500000 (0.12%)

french.wav

DeepL: Translate results from French [FR] to Spanish [ES]

[00:00.000 --> 00:06.640] Whisper es un sistema de reconocimiento automático del habla entrenado con 680.000
[00:06.640 --> 00:10.720] horas de datos multilingües y multitarea recogidos de Internet.
[00:10.720 --> 00:16.000] Sostenemos que el uso de una cantidad tan grande y diversa de datos
[00:16.000 --> 00:20.500] es la razón por la que el sistema es capaz de entender muchos acentos
[00:20.500 --> 00:24.880] a pesar del ruido de fondo, comprender vocabulario técnico y traducir con éxito
[00:24.880 --> 00:27.640] de varios idiomas al inglés.
[00:27.640 --> 00:33.360] Publicamos como código abierto el código fuente de nuestros modelos y de la inferencia
[00:33.360 --> 00:37.040] para que puedan servir como punto de partida para crear aplicaciones útiles
[00:37.040 --> 00:54.560] y para ayudar a avanzar en la investigación del procesamiento del habla.

DeepL: Character usage: 1327 / 500000 (0.27%)

Writing translated results...

audio_transcription/chinese_Spanish.txt
audio_transcription/chinese_Spanish.vtt
audio_transcription/chinese_Spanish.srt

audio_transcription/bruce_Spanish.txt
audio_transcription/bruce_Spanish.vtt
audio_transcription/bruce_Spanish.srt

audio_transcription/english_japanese_Spanish.txt
audio_transcription/english_japanese_Spanish.vtt
audio_transcription/english_japanese_Spanish.srt

audio_transcription/french_Spanish.txt
audio_transcription/french_Spanish.vtt
audio_transcription/french_Spanish.srt
```

[**See all output files**](https://github.com/Carleslc/AudioToText/blob/master/examples/multiple-files/audio_transcription)
