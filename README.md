# AudioToText

[![Google Colab Badge](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=fff&style=for-the-badge)](https://colab.research.google.com/github/Carleslc/AudioToText/blob/master/AudioToText.ipynb)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/carleslc)

**Transcribe** audio using [**Whisper**](https://github.com/openai/whisper) from [OpenAI](https://openai.com/).

**Translate** audio using [**Whisper**](https://github.com/openai/whisper) and [**DeepL**](https://www.deepl.com/) translator.

Generate _captions_ using VTT or SRT file formats.

[**Introducing Whisper** _(OpenAI Blog)_](https://openai.com/blog/whisper/)

[🇪🇸 Vídeo sobre Whisper _(Dot CSV)_](https://www.youtube.com/watch?v=JuMEmF-2FsA)

## How to use

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Carleslc/AudioToText/blob/master/AudioToText.ipynb)

**Open [AudioToText in Google Colab](https://colab.research.google.com/github/Carleslc/AudioToText/blob/master/AudioToText.ipynb) and follow the step-by-step instructions.**

A Cloud GPU will be assigned to you to execute the notebook code to transcribe and translate your audio files.

If you want to execute the notebook in your own computer check [_**Local installation**_](#local-installation-for-users-with-a-powerful-gpu).

## Features

1. All the [Whisper](https://github.com/openai/whisper) features:

![Whisper Features](https://cdn.openai.com/whisper/draft-20220920a/asr-training-data-desktop.svg)

- [**English transcription**](#audio-transcription-from-english-using-whisper)
- [**Non-English transcription**](#audio-transcription-from-almost-any-language-using-whisper)
- [**Any-to-English translation**](#audio-translation-to-english-using-whisper)

2. [**Any-to-Any\* translation**](#audio-translation-using-deepl-translator)
   
   Translate the transcriptions using [**DeepL**](https://www.deepl.com/) translator.

   [_\* See supported languages by DeepL_](https://support.deepl.com/hc/en-us/articles/360019925219-Languages-included-in-DeepL-Pro)

3. Save transcriptions and captions in TXT, VTT, SRT, TSV and JSON

### Audio **transcription** from English using Whisper

`task`: `Transcribe`

`language`: `Auto-Detect` or select `English` (recommended when using _`use_model`_ `tiny`, `base`, `small`, or `medium`)

### Audio **transcription** from [almost any language](https://github.com/openai/whisper#available-models-and-languages) using Whisper

`task`: `Transcribe`

`language`: `Auto-Detect` or select the source language of your audio file

<details>
  <summary><i>Supported source languages by Whisper</i></summary>
  
  ```
  Afrikaans
  Albanian
  Amharic
  Arabic
  Armenian
  Assamese
  Azerbaijani
  Bashkir
  Basque
  Belarusian
  Bengali
  Bosnian
  Breton
  Bulgarian
  Burmese
  Castilian
  Catalan
  Chinese
  Croatian
  Czech
  Danish
  Dutch
  English
  Estonian
  Faroese
  Finnish
  Flemish
  French
  Galician
  Georgian
  German
  Greek
  Gujarati
  Haitian
  Haitian Creole
  Hausa
  Hawaiian
  Hebrew
  Hindi
  Hungarian
  Icelandic
  Indonesian
  Italian
  Japanese
  Javanese
  Kannada
  Kazakh
  Khmer
  Korean
  Lao
  Latin
  Latvian
  Letzeburgesch
  Lingala
  Lithuanian
  Luxembourgish
  Macedonian
  Malagasy
  Malay
  Malayalam
  Maltese
  Maori
  Marathi
  Moldavian
  Moldovan
  Mongolian
  Myanmar
  Nepali
  Norwegian
  Nynorsk
  Occitan
  Panjabi
  Pashto
  Persian
  Polish
  Portuguese
  Punjabi
  Pushto
  Romanian
  Russian
  Sanskrit
  Serbian
  Shona
  Sindhi
  Sinhala
  Sinhalese
  Slovak
  Slovenian
  Somali
  Spanish
  Sundanese
  Swahili
  Swedish
  Tagalog
  Tajik
  Tamil
  Tatar
  Telugu
  Thai
  Tibetan
  Turkish
  Turkmen
  Ukrainian
  Urdu
  Uzbek
  Valencian
  Vietnamese
  Welsh
  Yiddish
  Yoruba
  ```
  
</details>

### Audio **translation to English** using Whisper

`task`: `Translate to English`

`language`: `Auto-Detect` or select the source language of your audio file

### Audio **translation** using [**DeepL**](https://www.deepl.com/) translator

Translation to other languages than English is not supported by _Whisper_.

However, as an alternative you can use [DeepL API](https://www.deepl.com/pro-api?cta=header-pro-api) to translate the transcription to [another language](https://support.deepl.com/hc/en-us/articles/360019925219-Languages-included-in-DeepL-Pro).

`task`: `Transcribe`

`language`: `Auto-Detect` or select the source language of your audio file \*

<details>
  <summary><i>Supported source languages by DeepL</i></summary>

  <a href="https://www.deepl.com/docs-api/translate-text"><code>source_lang</code></a>

  ```
  Bulgarian
  Chinese
  Czech
  Danish
  Dutch
  English
  Estonian
  Finnish
  French
  German
  Greek
  Hungarian
  Indonesian
  Italian
  Japanese
  Korean
  Latvian
  Lithuanian
  Norwegian
  Polish
  Portuguese
  Romanian
  Russian
  Slovak
  Slovenian
  Spanish
  Swedish
  Turkish
  Ukrainian
  ```
  
</details>

\* If the source language of your audio file is supported by Whisper but not supported by DeepL you can use the `Translate to English` task to generate an English transcription first and translate that to your desired target language using DeepL.

`deepl_api_key`: Your [DeepL API key](https://www.deepl.com/es/account/summary) generated after registering for a [DeepL Developer Account](https://www.deepl.com/pro-api).

`deepl_target_language`: Select your desired language

<details>
  <summary><i>Available target languages by DeepL</i></summary>
  
  <a href="https://www.deepl.com/docs-api/translate-text"><code>target_lang</code></a>
  
  ```
  Bulgarian
  Chinese (simplified)
  Czech
  Danish
  Dutch
  English (American)
  English (British)
  Estonian
  Finnish
  French
  German
  Greek
  Hungarian
  Indonesian
  Italian
  Japanese
  Latvian
  Lithuanian
  Polish
  Portuguese (Brazilian)
  Portuguese (European)
  Romanian
  Russian
  Slovak
  Slovenian
  Spanish
  Swedish
  Turkish
  Ukrainian
  ```
  
</details>

The [DeepL API](https://www.deepl.com/pro-api?cta=header-pro-api) has a free quota of **500,000 characters per month**.

If you exceed your free quota you can upgrade to _DeepL API Pro_ or try using the [Free Translator Files](https://www.deepl.com/translator/files) web feature uploading the generated transcripts.

### **Save transcripts** to different formats

`output_formats`: Select the desired transcript formats (comma-separated)

Available formats: **txt, vtt, srt, tsv, json**

[`txt`](https://en.wikipedia.org/wiki/Text_file) is recommended to read a transcription.

[`vtt`](https://en.wikipedia.org/wiki/WebVTT) or [`srt`](https://en.wikipedia.org/wiki/SubRip) are recommended to add **captions** to an audio or video.

Transcript files will be located in the _**`audio_transcription`**_ folder.

#### Add captions to VLC media player

If you use [VLC](https://www.videolan.org/) to play video or audio files, you can add your `vtt` or `srt` transcripts as captions by drag-and-drop the transcript file to the media player or go to _Subtitles -> Add Subtitle File_.

## Local installation (for users with a powerful GPU)

If you have a powerful computer with GPU hardware acceleration, you can also run the [_AudioToText notebook_](AudioToText.ipynb) in your local machine.

CPU execution is also available, but it is much slower and the [Cloud]((https://colab.research.google.com/github/Carleslc/AudioToText/blob/master/AudioToText.ipynb)) version is recommended if you do not have a decent GPU.

### Use Google Colab with your local environment

[Google Colab]((https://colab.research.google.com/github/Carleslc/AudioToText/blob/master/AudioToText.ipynb)) lets you connect to a local runtime using [Jupyter](http://jupyter.org/install).
This allows you to use the notebook using your local hardware and have access to your local file system.

[_How to set up and connect to a local runtime in Google Colab_](https://research.google.com/colaboratory/local-runtimes.html)

### Using [Jupyter Notebook](https://github.com/jupyter/notebook)

If you do not want to rely on Google Colab, you can just use the [Jupyter Notebook](https://docs.jupyter.org/) interface.

[_How to install Jupyter Notebook_](https://docs.jupyter.org/en/latest/install/notebook-classic.html)

Clone or download this repository and run inside the repository folder:

```sh
jupyter notebook AudioToText.ipynb
```

Or just run `jupyter notebook` without cloning this repository and _Upload_ the [`AudioToText.ipynb`](https://raw.githubusercontent.com/Carleslc/AudioToText/master/AudioToText.ipynb) file (_right-click -> Save as..._).

### Using [Jupyter Lab](https://github.com/jupyterlab/jupyterlab)

An alternative to the Jupyter Notebook interface is the [Jupyter Lab](https://jupyterlab.readthedocs.io/) interface.

[_How to install Jupyter Lab_](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

```sh
jupyter lab
```

Open the notebook using a URL:

_File -> Open from URL..._

```
https://raw.githubusercontent.com/Carleslc/AudioToText/master/AudioToText.ipynb
```

### Using [Python](https://www.python.org/downloads/) only

A plain [_python script_](audiototext.py) is also available to use without Jupyter.

```sh
python audiototext.py
```

### Using [Whisper CLI](https://github.com/openai/whisper#command-line-usage) only

If you do not need Cloud GPU and you do not want to translate using DeepL then you can just use the Whisper CLI in your console as follows:

#### Install [Whisper CLI](https://github.com/openai/whisper#setup) locally

1. Install [Python](https://www.python.org/downloads/)
2. Install [`ffmpeg`](https://ffmpeg.org/download.html)

  ```sh
  # on MacOS using Homebrew (https://brew.sh/)
  brew install ffmpeg

  # on Windows using Chocolatey (https://chocolatey.org/)
  choco install ffmpeg

  # on Ubuntu or Debian
  sudo apt update && sudo apt install ffmpeg

  # on Arch Linux
  sudo pacman -S ffmpeg
  ```

3. Install [Whisper CLI](https://github.com/openai/whisper#setup)
   
  ```sh
  # Install Whisper CLI
  pip install -U openai-whisper
  ```

#### [Whisper CLI usage](https://github.com/openai/whisper#command-line-usage) example

```sh
# Transcribe audio.mp3 and video.mp4 using large-v2 model
whisper audio.mp3 video.mp4 --model large-v2 --output_dir audio_transcription

# Translate japanese.wav from Japanese to English using small model
whisper japanese.wav --language Japanese --task translate --output_dir audio_transcription

# See all available options
whisper --help
```
