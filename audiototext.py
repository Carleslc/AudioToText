# -*- coding: utf-8 -*-
"""AudioToText CLI

Original file is located at https://colab.research.google.com/github/Carleslc/AudioToText/blob/master/AudioToText.ipynb

# 🗣️ [**AudioToText**](https://github.com/Carleslc/AudioToText)

### 🛠 [Whisper by OpenAI (GitHub)](https://github.com/openai/whisper)
"""

print("AudioToText CLI\n")

import argparse

parser = argparse.ArgumentParser(
  description="Transcribe and translate audio to text using Whisper and DeepL.",
  epilog=f'web: https://carleslc.me/AudioToText/'
)
parser.add_argument("audio_file", nargs='+', help="source file to transcribe")
parser.add_argument("--task", help="transcribe (default) or translate (to English)", default="transcribe", choices=["transcribe", "translate"])
parser.add_argument("--model", help="model to use (default: small)", default="small", choices=["tiny", "base", "small", "medium", "large-v1", "large-v2"])
parser.add_argument("--language", help="source file language (default: Auto-Detect)", default="Auto-Detect", choices=["Auto-Detect", "Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Assamese", "Azerbaijani", "Bashkir", "Basque", "Belarusian", "Bengali", "Bosnian", "Breton", "Bulgarian", "Burmese", "Castilian", "Catalan", "Chinese", "Croatian", "Czech", "Danish", "Dutch", "English", "Estonian", "Faroese", "Finnish", "Flemish", "French", "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian", "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Korean", "Lao", "Latin", "Latvian", "Letzeburgesch", "Lingala", "Lithuanian", "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Moldavian", "Moldovan", "Mongolian", "Myanmar", "Nepali", "Norwegian", "Nynorsk", "Occitan", "Panjabi", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Pushto", "Romanian", "Russian", "Sanskrit", "Serbian", "Shona", "Sindhi", "Sinhala", "Sinhalese", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili", "Swedish", "Tagalog", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Tibetan", "Turkish", "Turkmen", "Ukrainian", "Urdu", "Uzbek", "Valencian", "Vietnamese", "Welsh", "Yiddish", "Yoruba"])
parser.add_argument("--coherence_preference", help="True (default): More coherence, but may repeat text. False: Less repetitions, but may have less coherence", default='True', choices=[True, False], type=lambda b: b.lower() != 'false')
parser.add_argument("--output_formats", help="desired result formats (default: txt,vtt,srt,tsv,json)", default="txt,vtt,srt,tsv,json")
parser.add_argument("--output_dir", help="folder to save results (default: audio_transcription)", default="audio_transcription")
parser.add_argument("--deepl_api_key", help="DeepL API key, if you want to translate results using DeepL. Get a DeepL Developer Account API Key: https://www.deepl.com/pro-api")
parser.add_argument("--deepl_target_language", help="results target language if you want to translate results using DeepL (--deepl_api_key required)", choices=["Bulgarian", "Chinese", "Chinese (simplified)", "Czech", "Danish", "Dutch", "English", "English (American)", "English (British)", "Estonian", "Finnish", "French", "German", "Greek", "Hungarian", "Indonesian", "Italian", "Japanese", "Korean", "Latvian", "Lithuanian", "Norwegian", "Polish", "Portuguese", "Portuguese (Brazilian)", "Portuguese (European)", "Romanian", "Russian", "Slovak", "Slovenian", "Spanish", "Swedish", "Turkish", "Ukrainian"])
parser.add_argument("--deepl_coherence_preference", help="True (default): Share context between lines while translating. False: Translate each line independently", default='True', choices=[True, False], type=lambda b: b.lower() != 'false')
parser.add_argument("--deepl_formality", help="whether the translated text should lean towards formal or informal language (languages with formality supported: German,French,Italian,Spanish,Dutch,Polish,Portuguese,Russian)", default="default", choices=["default", "formal", "informal"])
args = parser.parse_args()

"""
## [Step 1] ⚙️ Install the required libraries
"""

import os, subprocess

from sys import platform as sys_platform

status, ffmpeg_version = subprocess.getstatusoutput("ffmpeg -version")

if status != 0:
  from platform import platform

  if sys_platform == 'linux' and 'ubuntu' in platform().lower():
    os.system("apt install ffmpeg")
  else:
    print("Install ffmpeg: https://ffmpeg.org/download.html")
    exit(status)
else:
  print(ffmpeg_version.split('\n')[0])

os.system("pip install git+https://github.com/openai/whisper.git@7858aa9c08d98f75575035ecd6481f462d66ca27 numpy torch deepl")

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

3.3. Run this script and wait for the transcription to complete.

  - You can try other parameters if the result with default parameters does not suit your needs.

  If the execution takes too long to complete you can choose a smaller model in `use_model`, with an accuracy tradeoff.

  [Available models and languages](https://github.com/openai/whisper#available-models-and-languages)

  If the source audio file is entirely in English setting the `language` to English may provide better results when using a non-large model.
  
  More parameters are available in the code `options` object.
"""

import whisper
from whisper.utils import format_timestamp, get_writer, WriteTXT

import numpy as np

import torch

# select task

task = args.task

# set audio file path

audio_files = args.audio_file

# set model

use_model = args.model

# detect device

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"\nUsing {'GPU' if DEVICE == 'cuda' else 'CPU ⚠️'}")

# https://medium.com/analytics-vidhya/the-google-colab-system-specification-check-69d159597417
if DEVICE == "cuda":
  os.system('nvidia-smi -L')
else:
  if sys_platform == 'linux':
    os.system('lscpu | grep "Model name" | awk \'{$1=$1};1\'')

  if use_model not in ['tiny', 'base', 'small']:
    print("Not using GPU can result in a very slow execution")
    print("You may want to try a smaller model (tiny, base, small)")

# select language

WHISPER_LANGUAGES = [k.title() for k in whisper.tokenizer.TO_LANGUAGE_CODE.keys()]

language = args.language

if language == "Auto-Detect":
  language = "detect"

if language and language != "detect" and language not in WHISPER_LANGUAGES:
  print(f"\nLanguage '{language}' is invalid")
  language = "detect"

if language and language != "detect":
  print(f"\nLanguage: {language}")

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

# coherence_preference = "More coherence, but may repeat text" #@param ["More coherence, but may repeat text", "Less repetitions, but may have less coherence"]

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
    'condition_on_previous_text': args.coherence_preference,
}

if DEVICE == 'cpu':
  torch.set_num_threads(os.cpu_count())

# execute task
# !whisper "{audio_file}" --task {task} --model {use_model} --output_dir {output_dir} --device {DEVICE} --verbose {options['verbose']}

if task == "translate":
  print("-- TRANSLATE TO ENGLISH --")
else:
  print("-- TRANSCRIPTION --")

results = {} # audio_path to result

for audio_path in audio_files:
  audio_path = audio_path.strip()
  
  print(f"\nProcessing: {audio_path}\n")

  # detect language
  detect_language = not language or language == "detect"
  if detect_language:
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)

    language_code = max(probs, key=probs.get)
    options['language'] = whisper.tokenizer.LANGUAGES[language_code].title()
    
    print(f"Detected language: {options['language']}\n")
  else:
    options['language'] = language

  # transcribe
  result = whisper.transcribe(model, audio_path, **options)

  for segment in result['segments']:
    segment['text'] = segment['text'].strip()
  
  result['text'] = '\n'.join(map(lambda segment: segment['text'], result['segments']))

  results[audio_path] = result

"""## [Step 4] 💾 **Save results**

Run this cell to write the transcription as a file output.

Results will be available in the **audio_transcription** folder in the formats selected in `output_formats`.

If you don't see that folder, you may need to refresh 🔄 the Files folder.

Available formats: `txt,vtt,srt,tsv,json`
"""

# set output folder
output_dir = args.output_dir

# set output formats: https://github.com/openai/whisper/blob/7858aa9c08d98f75575035ecd6481f462d66ca27/whisper/utils.py#L145
output_formats = args.output_formats
output_formats = output_formats.split(',')

from typing import TextIO

class WriteText(WriteTXT):

  def write_result(self, result: dict, file: TextIO):
    print(result['text'], file=file, flush=True)

def write_result(result, output_format, output_file_name):
  output_format = output_format.strip()

  # start captions in non-zero timestamp (some media players does not detect the first caption)
  fix_vtt = output_format == 'vtt' and result['segments'] and result['segments'][0].get('start') == 0
  
  if fix_vtt:
    result['segments'][0]['start'] += 1/1000 # +1ms

  # write result in the desired format
  writer = WriteText(output_dir) if output_format == 'txt' else get_writer(output_format, output_dir)
  writer(result, output_file_name)

  if fix_vtt:
    result['segments'][0]['start'] = 0 # reset change

  output_file_path = os.path.join(output_dir, f"{output_file_name}.{output_format}")
  print(output_file_path)

# save results

print("\nWriting results...")

os.makedirs(output_dir, exist_ok=True)

for audio_path, result in results.items():
  print(end='\n')
  
  output_file_name = os.path.splitext(os.path.basename(audio_path))[0]

  for output_format in output_formats:
    write_result(result, output_format, output_file_name)

"""## [Step 5] 💬 Translate results with DeepL (API key needed)

This is an **optional** step to translate the transcription to another language using the **DeepL** API.

[Get a DeepL Developer Account API Key](https://www.deepl.com/pro-api)

Set the `deepl_api_key` to translate the transcription to a supported language in `deepl_target_language`.
"""

import deepl

# translation service options (DeepL Developer Account)

deepl_api_key = args.deepl_api_key

deepl_target_language = args.deepl_target_language

deepl_coherence_preference = args.deepl_coherence_preference

deepl_formality = "default"

if deepl_api_key and not deepl_target_language:
  deepl_target_language = 'English'

if deepl_target_language:
  if not deepl_api_key:
    print("\nRequired: --deepl_api_key")
    print("Get a DeepL Developer Account API Key: https://www.deepl.com/pro-api")
  elif deepl_target_language == 'English':
    deepl_target_language = "English (British)"
  elif deepl_target_language == 'Chinese':
    deepl_target_language = "Chinese (simplified)"
  elif deepl_target_language == 'Portuguese':
    deepl_target_language = "Portuguese (European)"

use_deepl_translation = deepl_api_key and deepl_target_language

if use_deepl_translation:
  print(end='\n')

  if args.deepl_formality != 'default':
    deepl_formality = 'prefer_more' if args.deepl_formality == 'formal' else 'prefer_less'

  translated_results = {} # audio_path to translated results

  try:
    deepl_translator = deepl.Translator(deepl_api_key)

    deepl_source_languages = [lang.code.upper() for lang in deepl_translator.get_source_languages()]
    
    deepl_target_languages_dict = deepl_translator.get_target_languages()
    deepl_target_languages = [lang.name for lang in deepl_target_languages_dict]

    deepl_target_language_code = next(lang.code for lang in deepl_target_languages_dict if lang.name == deepl_target_language).upper()
    target_language_code = deepl_target_language_code.split('-')[0]
    
    for audio_path, result in results.items():
      deepl_usage = deepl_translator.get_usage()
      
      if deepl_usage.any_limit_reached:
        print(audio_path)
        raise deepl.DeepLException("Quota for this billing period has been exceeded, message: Quota Exceeded")
      else:
        print(audio_path + '\n')
      
      # translate results (DeepL)
      source_language_code = whisper.tokenizer.TO_LANGUAGE_CODE.get(result['language'].lower()).upper()

      if (task == 'translate' and target_language_code != 'EN') or (task == 'transcribe' and source_language_code in deepl_source_languages and source_language_code != target_language_code):
        source_lang = source_language_code if task == 'transcribe' else None
        translate_from = f"from {result['language']} [{source_language_code}] " if source_lang else ''
        print(f"DeepL: Translate results {translate_from}to {deepl_target_language} [{deepl_target_language_code}]\n")

        segments = result['segments']

        translated_results[audio_path] = { 'text': '', 'segments': [], 'language': deepl_target_language }

        # segments / request (max 128 KiB / request, so deepl_batch_requests_size is limited to around 1000)
        deepl_batch_requests_size = 200 # 200 segments * ~100 bytes / segment = ~20 KB / request  (~15 minutes of speech)
        
        for batch_segments in [segments[i:i + deepl_batch_requests_size] for i in range(0, len(segments), deepl_batch_requests_size)]:
          batch_segments_text = [segment['text'] for segment in batch_segments]

          if deepl_coherence_preference:
            batch_segments_text = '<br/>'.join(batch_segments_text)

          # DeepL request
          deepl_results = deepl_translator.translate_text(
              text=batch_segments_text,
              source_lang=source_lang,
              target_lang=deepl_target_language_code,
              formality=deepl_formality,
              split_sentences='nonewlines',
              tag_handling='xml' if deepl_coherence_preference else None,
              ignore_tags='br' if deepl_coherence_preference else None, # used to synchronize sentences with whisper lines but without splitting sentences in DeepL
              outline_detection=False if deepl_coherence_preference else None
          )
          
          deepl_results_segments = deepl_results.text.split('<br/>') if deepl_coherence_preference else [deepl_result_segment.text for deepl_result_segment in deepl_results]

          for j, translated_text in enumerate(deepl_results_segments):
            segment = batch_segments[j]

            # fix sentence formatting
            translated_text = translated_text.lstrip(',.。 ').rstrip()

            if not deepl_coherence_preference and translated_text and translated_text[-1] in '.。' and segment['text'][-1] not in '.。':
              translated_text = translated_text[:-1]

            # add translated segments
            translated_results[audio_path]['segments'].append(dict(id=segment['id'], start=segment['start'], end=segment['end'], text=translated_text))

            if options['verbose']:
              print(f"[{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}] {translated_text}")
        
        deepl_usage = deepl_translator.get_usage()
        
        if deepl_usage.character.valid:
          print(f"\nDeepL: Character usage: {deepl_usage.character.count} / {deepl_usage.character.limit} ({100*(deepl_usage.character.count/deepl_usage.character.limit):.2f}%)\n")
      elif source_language_code == target_language_code:
        print(f"Nothing to translate. Results are already in {result['language']}.")
      elif task == 'transcribe' and source_language_code not in deepl_source_languages:
        print(f"DeepL: {result['language']} is not yet supported")
  except deepl.DeepLException as e:
    if isinstance(e, deepl.AuthorizationException) and str(e) == "Authorization failure, check auth_key":
      e = "Authorization failure, check deepl_api_key"
    print(f"\nDeepL: [Error] {e}\n")
  
  # save translated results (if any)

  if translated_results:
    print("Writing translated results...")

    for audio_path, translated_result in translated_results.items():
      print(end='\n')

      translated_result['text'] = '\n'.join(map(lambda translated_segment: translated_segment['text'], translated_result['segments']))
      
      output_file_name = os.path.splitext(os.path.basename(audio_path))[0]
      translated_output_file_name = f"{output_file_name}_{deepl_target_language}"

      for output_format in output_formats:
        write_result(translated_result, output_format, translated_output_file_name)
