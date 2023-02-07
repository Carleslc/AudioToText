# -*- coding: utf-8 -*-
"""AudioToText

Original file is located at https://colab.research.google.com/github/Carleslc/AudioToText/blob/master/AudioToText.ipynb

# 🗣️ [**AudioToText**](https://github.com/Carleslc/AudioToText)

### 🛠 [Whisper by OpenAI (GitHub)](https://github.com/openai/whisper)

## [Step 1] ⚙️ Install the required libraries
"""

import os, subprocess

status, ffmpeg_version = subprocess.getstatusoutput("ffmpeg -version")

if status != 0:
  print("Install ffmpeg: https://ffmpeg.org/download.html")
  exit(status)
else:
  print(ffmpeg_version.split('\n')[0])

os.system("pip install git+https://github.com/openai/whisper.git deepl numpy torch")

"""## [Step 2] 📁 Upload your audio files to this folder

Almost any audio or video file format is [supported](https://gist.github.com/Carleslc/1d6b922c8bf4a7e9627a6970d178b3a6).

## [Step 3] 👂 Transcribe or Translate

3.1. Choose a `task`:
  - `Transcribe` speech to text in the same language of the source audio file.
  - `Translate to English` speech to text in English.
  
Translation to other languages is not supported with _Whisper_ by default.
You may try to choose the _Transcribe_ task and set your desired `language`, but translation is not guaranteed. However, you can use **_DeepL_** later in the Step 5 to translate the transcription to another language.

3.2. Edit the `audio_file` to match your uploaded file name to transcribe.

- If you want to transcribe multiple files with the same parameters you must separate their file names with commas `,`

3.3. Run this cell and wait for the transcription to complete.

  - You can try other parameters if the result with default parameters does not suit your needs.

  If the execution takes too long to complete you can choose a smaller model in `use_model`, with an accuracy tradeoff.

  [Available models and languages](https://github.com/openai/whisper#available-models-and-languages)

  If the source audio file is entirely in English setting the `language` to English may provide better results when using a non-large model.
  
  More parameters are available in the code `options` object.
"""

# import modules

import whisper
from whisper.utils import format_timestamp, get_writer

import numpy as np

import torch

# detect device

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using {'GPU' if DEVICE == 'cuda' else 'CPU ⚠️'}")

# https://medium.com/analytics-vidhya/the-google-colab-system-specification-check-69d159597417
if DEVICE == "cuda":
  os.system('nvidia-smi -L')
else:
  os.system('lscpu | grep "Model name"')
  print("Not using GPU can result in a very slow execution")

# select task

task = "Transcribe" #@param ["Transcribe", "Translate to English"]

task = "transcribe" if task == "Transcribe" else "translate"

# set audio file path

audio_file = "audio.mp3" #@param {type:"string"}

audio_files = audio_file.split(',')

# set model

use_model = "small" #@param ["tiny", "base", "small", "medium", "large-v1", "large-v2"]

# select language

WHISPER_LANGUAGES = [k.title() for k in whisper.tokenizer.TO_LANGUAGE_CODE.keys()]

language = "Auto-Detect" #@param ["Auto-Detect", "Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Assamese", "Azerbaijani", "Bashkir", "Basque", "Belarusian", "Bengali", "Bosnian", "Breton", "Bulgarian", "Burmese", "Castilian", "Catalan", "Chinese", "Croatian", "Czech", "Danish", "Dutch", "English", "Estonian", "Faroese", "Finnish", "Flemish", "French", "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian", "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Korean", "Lao", "Latin", "Latvian", "Letzeburgesch", "Lingala", "Lithuanian", "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Moldavian", "Moldovan", "Mongolian", "Myanmar", "Nepali", "Norwegian", "Nynorsk", "Occitan", "Panjabi", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Pushto", "Romanian", "Russian", "Sanskrit", "Serbian", "Shona", "Sindhi", "Sinhala", "Sinhalese", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili", "Swedish", "Tagalog", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Tibetan", "Turkish", "Turkmen", "Ukrainian", "Urdu", "Uzbek", "Valencian", "Vietnamese", "Welsh", "Yiddish", "Yoruba"]

if language == "Auto-Detect":
  language = "detect"

if language and language != "detect" and language not in WHISPER_LANGUAGES:
  print(f"Language '{language}' is invalid")
  language = "detect"

if language and language != "detect":
  print(f"Language: {language}\n")

# load model

MODELS_WITH_ENGLISH_VERSION = ["tiny", "base", "small", "medium"]

if language == "English" and use_model in MODELS_WITH_ENGLISH_VERSION:
  use_model += ".en"

print(f"\nLoading {use_model} model...")

model = whisper.load_model(use_model, device=DEVICE)

print(
    f"Model {use_model} is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,d} parameters.\n"
)

# set options

coherence_preference = "More coherence, but may repeat text" #@param ["More coherence, but may repeat text", "Less repetitions, but may have less coherence"]

## Info: https://github.com/openai/whisper/blob/main/whisper/transcribe.py#L19
options = {
    'task': task,
    'verbose': True,
    'fp16': DEVICE == 'cuda',
    'best_of': 5,
    'beam_size': 5,
    'patience': None,
    'length_penalty': None,
    'suppress_tokens': '-1',
    'temperature': (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
    'condition_on_previous_text': coherence_preference == "More coherence, but may repeat text",
}

if DEVICE == 'cpu':
  torch.set_num_threads(os.cpu_count())

# execute task
# !whisper "{audio_file}" --task {task} --model {use_model} --output_dir {output_dir} --device {DEVICE} --verbose {options['verbose']}

if task == "translate":
  print("-- TRANSLATE TO ENGLISH --\n")
else:
  print("-- TRANSCRIPTION --\n")

results = {} # audio_path to result

for audio_path in audio_files:
  print(f"Processing: {audio_path}")

  # detect language
  detect_language = not language or language == "detect"
  if detect_language:
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_file)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)

    language_code = max(probs, key=probs.get)
    options['language'] = whisper.tokenizer.LANGUAGES[language_code].title()
    
    print(f"Detected language: {options['language']}")
  else:
    options['language'] = language

  # transcribe
  results[audio_path] = whisper.transcribe(model, audio_path, **options)

"""## [Step 4] 💾 **Save results**

Run this cell to write the transcription as a file output.

Results will be available in the **audio_transcription** folder in the formats selected in `output_formats`.

If you don't see that folder, you may need to refresh 🔄 the Files folder.

Available formats: `txt,vtt,srt,tsv,json`
"""

# set output folder
output_dir = "audio_transcription"

# set output formats: https://github.com/openai/whisper/blob/7858aa9c08d98f75575035ecd6481f462d66ca27/whisper/utils.py#L145
output_formats = "txt,vtt,srt,tsv,json" #@param ["txt,vtt,srt,tsv,json", "txt,vtt", "txt", "vtt", "srt", "tsv", "json"] {allow-input: true}
output_formats = output_formats.split(',')

# save results

print("Writing results...\n")

os.makedirs(output_dir, exist_ok=True)

for audio_path, result in results.items():
  output_file_name = os.path.splitext(os.path.basename(audio_path))[0]

  for output_format in output_formats:
    output_format = output_format.strip()

    output_file_path = os.path.join(output_dir, f"{output_file_name}.{output_format}")
    print(output_file_path)

    writer = get_writer(output_format, output_dir)
    writer(result, output_file_name)

"""## [Step 5] 💬 Translate results with DeepL (API key needed)

This is an **optional** step to translate the transcription to another language using the **DeepL** API.

[Get a DeepL Developer Account API Key](https://www.deepl.com/pro-api?cta=header-pro-api)

Set the `deepl_api_key` to translate the transcription to a supported language in `deepl_target_language`.
"""

# install dependencies
import deepl

# translation service options (DeepL Developer Account)

deepl_api_key = "" #@param {type:"string"}
deepl_target_language = "" #@param ["", "Bulgarian", "Chinese (simplified)", "Czech", "Danish", "Dutch", "English (American)", "English (British)", "Estonian", "Finnish", "French", "German", "Greek", "Hungarian", "Indonesian", "Italian", "Japanese", "Latvian", "Lithuanian", "Polish", "Portuguese (Brazilian)", "Portuguese (European)", "Romanian", "Russian", "Slovak", "Slovenian", "Spanish", "Swedish", "Turkish", "Ukrainian"]

use_deepl_translation = deepl_api_key and deepl_target_language

if not use_deepl_translation:
  if not deepl_api_key:
    print("Required: deepl_api_key")
    print("Get a DeepL Developer Account API Key: https://www.deepl.com/pro-api?cta=header-pro-api")
  if not deepl_target_language:
    print("Required: deepl_target_language")
else:
  translated_results = { "segments": [] }

  try:
    deepl_translator = deepl.Translator(deepl_api_key)

    deepl_source_languages = [lang.code.upper() for lang in deepl_translator.get_source_languages()]
    
    deepl_target_languages_dict = deepl_translator.get_target_languages()
    deepl_target_languages = [lang.name for lang in deepl_target_languages_dict]

    deepl_target_language_code = next(lang.code for lang in deepl_target_languages_dict if lang.name == deepl_target_language).upper()

    deepl_usage = deepl_translator.get_usage()
    
    if deepl_usage.any_limit_reached:
        print('DeepL: Translation limit reached.')
        use_deepl_translation = False

    # translate results (DeepL)
    if use_deepl_translation:
      source_language_code = whisper.tokenizer.TO_LANGUAGE_CODE.get(options['language'].lower()).upper()
      target_language_code = deepl_target_language_code.split('-')[0]

      if (task == 'translate' and target_language_code != 'EN') or (task == 'transcribe' and source_language_code in deepl_source_languages and source_language_code != target_language_code):
        source_lang = source_language_code if task == 'transcribe' else None
        translate_from = f"from {options['language']} [{source_language_code}] " if source_lang else ''
        print(f"DeepL: Translate results {translate_from}to {deepl_target_language} [{deepl_target_language_code}]\n")

        segments = result["segments"]
        deepl_batch_requests_size = 10
        
        for batch_segments in [segments[i:i + deepl_batch_requests_size] for i in range(0, len(segments), deepl_batch_requests_size)]:
          deepl_results = deepl_translator.translate_text([segment['text'] for segment in batch_segments], source_lang=source_lang, target_lang=deepl_target_language_code, split_sentences='off')
          
          for j, deepl_result in enumerate(deepl_results):
            segment = batch_segments[j]
            translated_text = deepl_result.text
            translated_results["segments"].append(dict(id=segment['id'], start=segment['start'], end=segment['end'], text=translated_text))

            if options['verbose']:
              print(f"[{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}] {translated_text}")

        deepl_usage = deepl_translator.get_usage()
        
        if deepl_usage.character.valid:
          print(f"\nDeepL: Character usage: {deepl_usage.character.count} / {deepl_usage.character.limit} ({100*(deepl_usage.character.count/deepl_usage.character.limit):.1f}%)\n")
      elif task == 'transcribe' and source_language_code not in deepl_source_languages:
        print(f"DeepL: {options['language']} is not yet supported")
  except deepl.DeepLException as e:
    if isinstance(e, deepl.AuthorizationException) and str(e) == "Authorization failure, check auth_key":
      e = "Authorization failure, check deepl_api_key"
    print(f"DeepL: [Error] {e}")
  
  # save translated results (if any)

  if translated_results["segments"]:
    print("Writing translated results...\n")

    for output_format in output_formats:
      output_format = output_format.strip()

      translated_output_file_name = f"{output_file_name}_{deepl_target_language}"
      translated_output_file_path = os.path.join(output_dir, f"{translated_output_file_name}.{output_format}")

      print(translated_output_file_path)

      writer = get_writer(output_format, output_dir)
      writer(translated_results, translated_output_file_name)
