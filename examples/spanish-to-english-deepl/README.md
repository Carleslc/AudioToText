## Example: Spanish to English using DeepL

This example transcribes the audio of a spanish video file (low-res so it can be uploaded fast) using Whisper to its source language in TXT, VTT and SRT formats.

Then uses DeepL API to translate the generated transcripts to english.

## Input

**task**: `Transcribe`

**audio_file**: [`Whisper-Example.3gp`](https://carleslc.me/AudioToText/examples/spanish-to-english-deepl/Whisper-Example.3gp) ([Original YouTube video](https://www.youtube.com/watch?v=JuMEmF-2FsA))

**use_model**: `large-v2`

**language:** `Auto-Detect` (Spanish)

## Output

```
Using GPU
GPU 0: Tesla T4 (UUID: GPU-cef38425-c7cc-b5d1-e67a-bb320d3c2cb0)

Loading large-v2 model...
100%|██████████████████████████████████████| 2.87G/2.87G [00:27<00:00, 114MiB/s]
Model large-v2 is multilingual and has 1,541,384,960 parameters.

-- TRANSCRIPTION --

Processing: Whisper-Example.3gp

Detected language: Spanish

[00:00.000 --> 00:06.040]  2022 será recordado como el año de Stable Diffusion, de Dalí 2, de increíbles modelos
[00:06.040 --> 00:10.160]  generadores de texto como Palm o generadores de código como AlphaCode.
[00:10.160 --> 00:13.920]  Y sin embargo, charlando el mes pasado con Andrés Torrubia, él me comentaba que lo
[00:13.920 --> 00:18.120]  más interesante que había visto este año era una inteligencia artificial que venía
[00:18.120 --> 00:21.880]  del laboratorio OpenAI, una IA llamada Whisper.
[00:21.880 --> 00:26.880]  ¿Qué es para ti de lo que ha salido este año lo más impresionante?
[00:26.880 --> 00:31.800]  Pues curiosamente, fíjate, curiosamente, hasta ahora Whisper, yo creo.
[00:31.800 --> 00:32.800]  ¿Sabes por qué?
[00:32.800 --> 00:33.800]  Curioso, eh.
[00:33.800 --> 00:39.760]  Por lo que me impresiona Whisper es que Whisper funciona, es como, para mí, Whisper, si fuera
[00:39.760 --> 00:46.880]  el coche autónomo, sería el primer self-driving del dictado, o sea, es el primero que se parece
[00:46.880 --> 00:47.880]  a una persona.
[00:47.880 --> 00:51.000]  Bueno, pero para que entiendas tú primero qué es esto de Whisper, te voy a pedir que
[00:51.000 --> 00:53.120]  hagas el siguiente ejercicio.
[00:53.120 --> 00:57.800]  Te voy a reproducir un audio en inglés y tu tarea es transcribir cada una de las palabras
[00:57.800 --> 00:59.600]  que estés escuchando.
[00:59.600 --> 01:00.600]  ¿Estás listo?
[01:00.600 --> 01:02.600]  Tres, dos, uno.
[01:19.800 --> 01:21.280]  ¿Has entendido algo?
[01:21.280 --> 01:22.760]  Ya, yo tampoco.
[01:22.760 --> 01:28.160]  Pues a oídos de esta inteligencia artificial, esta es la transcripción perfecta que ha conseguido.
[01:28.160 --> 01:29.400]  ¿Y qué tal tu coreano?
[01:29.400 --> 01:33.680]  Bueno, pues para Whisper tampoco es problema y también puede transcribir este audio en
[01:33.680 --> 01:35.520]  perfecto inglés.
[01:44.440 --> 01:46.080]  Y bueno, también me entiende a mí.
[01:46.080 --> 01:50.040]  Esto que estás viendo en pantalla ahora es el speech to text que consigue Whisper cuando
[01:50.040 --> 01:52.680]  le paso la pista de audio que estás escuchando.
[01:52.680 --> 01:57.440]  Fíjate bien, no sólo consigue una transcripción casi perfecta, entendiendo incluso palabras
[01:57.440 --> 02:02.760]  concretas como Whisper o speech to text, sino que también es capaz de generar puntos, comas
[02:02.760 --> 02:06.560]  y otros signos de puntuación que a otros muchos modelos comerciales de reconocimiento
[02:06.560 --> 02:08.360]  del habla pues se le suele atragantar.
[02:08.360 --> 02:10.720]  Y esto es muy interesante.
[02:10.720 --> 02:12.960]  Bueno, no esto, sino Whisper.
[02:12.960 --> 02:18.160]  Whisper en general tiene muchas cosas interesantes y la primera cosa interesante es el contexto
[02:18.160 --> 02:20.120]  en el que esta herramienta aparece.
[02:20.120 --> 02:23.640]  Tras un año de increíbles logros por parte del Laboratorio de Inteligencia Artificial
[02:23.640 --> 02:29.680]  de OpenAI, de repente de la nada surge una iniciativa colaborativa como Stability.ai
[02:29.680 --> 02:34.320]  que en septiembre toma por bandera el hacer open source muchas de las tecnologías que
[02:34.320 --> 02:40.240]  OpenAI por su parte pues ha decidido guardarse para sí y compartir sólo bajo servicios
[02:40.240 --> 02:41.240]  de pago.
[02:41.240 --> 02:46.360]  Para mí esto tampoco es un problema, puesto que al final OpenAI como empresa pues tiene
[02:46.360 --> 02:50.720]  que pagar sus facturas y al menos nos está dando una forma de acceder a estas potentes
[02:50.720 --> 02:52.360]  inteligencias artificiales.
[02:52.360 --> 02:53.920]  Aprende Google.
[02:53.920 --> 02:57.880]  Pero claro, llega un muchachito nuevo a la ciudad y empieza a regalar caramelos a los
[02:57.880 --> 03:01.920]  niños y de repente el chico popular pues empieza a ver desplazado.
[03:01.920 --> 03:07.760]  Y en ese preciso momento llega OpenAI de la nada y nos regala a Whisper para beneficio
[03:07.760 --> 03:08.760]  de todos.
[03:08.760 --> 03:13.580]  Porque sí, amigos, esto es open source, que sé que os encanta escuchar estas palabras.
[03:13.580 --> 03:17.160]  Al final del vídeo voy a enseñar un mini tutorial para que veáis qué sencillo es utilizar
[03:17.160 --> 03:21.000]  esta herramienta y también os voy a compartir un notebook para que sea súper sencillo para
[03:21.000 --> 03:22.000]  vosotros.
[03:22.000 --> 03:25.800]  Y esto es lo que hace a Whisper una herramienta súper interesante, pero no es la única cosa.
[03:25.800 --> 03:29.800]  Y aquí es donde viene una de las cosas que más ha llamado mi atención y es que Whisper
[03:29.800 --> 03:34.440]  no es un complejo sistema que hayan diseñado para procesar audio como nunca antes había
[03:34.440 --> 03:38.640]  hecho o un sistema súper complejo con un montón de módulos de procesamiento.
[03:38.640 --> 03:45.840]  No, Whisper es esto de aquí, una red neuronal de tipo transformer de las de 2017, no tiene
[03:45.840 --> 03:47.920]  ningún cambio, ninguna novedad.
[03:47.920 --> 03:51.280]  Es una arquitectura que ya todos nosotros conocemos.
[03:51.280 --> 03:55.800]  Entonces, si esto es así, por qué no existía ya una tecnología como Whisper?
[03:55.800 --> 04:00.800]  Pues la clave que hace a Whisper algo tan potente está en los datos y en cómo han
[04:00.800 --> 04:02.920]  estructurado su entrenamiento.
[04:02.920 --> 04:09.040]  Para entrenarlo, OpenAI ha utilizado ni más ni menos que 680.000 horas de audio con su
[04:09.040 --> 04:12.360]  correspondiente texto, una brutalidad.
[04:12.360 --> 04:17.200]  Y es que si hacéis el cálculo 680.000 horas y empezar a reproducirlas ahora, acabarías
[04:17.200 --> 04:19.880]  de escucharla dentro de 77 años.
[04:19.880 --> 04:24.160]  Te podrías asegurar que en algún momento en el cielo verías surcar al cometa Halley.
[04:24.160 --> 04:28.560]  Pero es que además, una cosa muy interesante es que estos audios vienen en múltiples idiomas,
[04:28.560 --> 04:32.200]  permitiéndonos poder entrenar a un modelo que es multilinguaje, que puede entendernos
[04:32.200 --> 04:36.560]  si le hablamos en español, en inglés, en coreano, da igual.
[04:36.560 --> 04:38.240]  Pero la cosa no se queda solo ahí.
[04:38.240 --> 04:43.720]  Y es que Whisper, además de ser un sistema multilinguaje, también es un sistema multitarea.
[04:43.720 --> 04:47.520]  Esta es una tendencia que, como ya vimos en el vídeo sobre Gato, en el mundo del deep
[04:47.520 --> 04:49.760]  learning cada vez es más frecuente.
[04:49.760 --> 04:54.680]  No entrenar a la inteligencia artificial para una única tarea, sino entrenarla para varias
[04:54.680 --> 04:59.560]  diferentes, haciendo así que su aprendizaje sea mucho más sólido y robusto.
[04:59.560 --> 05:04.560]  Como hemos visto, Whisper puede tomar audios en inglés y transcribirlos al inglés, o
[05:04.560 --> 05:06.960]  audio en coreano y transcribirlo al coreano.
[05:06.960 --> 05:11.200]  Pero el mismo modelo también puede identificar qué lenguaje se está hablando, o actuar
[05:11.200 --> 05:15.360]  como un detector de voz para clasificar cuando en un trozo de audio se está escuchando no
[05:15.360 --> 05:16.360]  a una persona.
[05:16.360 --> 05:20.960]  O también, la tarea que más interesante me parece de todas, que tú le puedas hablar
[05:20.960 --> 05:25.720]  a Whisper en cualquier idioma y que él te lo transcriba automáticamente al inglés.
[05:25.720 --> 05:29.800]  Y en este caso no sabría deciros por qué, pero para mí esta me parece una funcionalidad
[05:29.800 --> 05:30.800]  fascinante.
[05:30.800 --> 05:32.880]  Parece que tampoco nos ofrece nada nuevo, ¿no?
[05:32.880 --> 05:37.560]  Al final tú puedes coger el texto que genera cualquier transcriptor de texto en tu idioma
[05:37.560 --> 05:39.520]  y pasarlo por un traductor.
[05:39.520 --> 05:43.520]  Pero en este caso me parece fascinante el ver cómo algo tan sencillo como un único
[05:43.520 --> 05:47.880]  modelo de deep learning te permite poder hablarle en cualquier idioma y que te genere el texto
[05:47.880 --> 05:51.520]  en inglés sin tener que combinar ningún tipo de herramientas.
[05:51.520 --> 05:53.400]  Es súper sencillo.
[05:53.400 --> 05:56.360]  Y lo de los datos que hemos comentado antes también es súper interesante.
[05:56.360 --> 06:00.480]  Porque mi primera intuición aquí es que OpenAI, en la búsqueda de un dataset masivo
[06:00.480 --> 06:05.280]  de estas 680.000 horas de audio que tuviera una transcripción de texto para poder hacer
[06:05.280 --> 06:09.800]  este aprendizaje supervisado, pues posiblemente había acudido a una de las mayores fuentes
[06:09.800 --> 06:12.520]  que podemos encontrar en Internet, que es YouTube.
[06:12.520 --> 06:16.960]  Al final ya sabéis que todos los vídeos de YouTube tienen generados subtítulos automáticamente.
[06:16.960 --> 06:17.960]  Pues no.
[06:17.960 --> 06:22.800]  Justamente en esto OpenAI hace mucho hincapié en su paper para explicarnos que han hecho
[06:22.800 --> 06:28.200]  un proceso de filtrado para eliminar del dataset cualquier aparición de texto generado por
[06:28.200 --> 06:31.000]  sistemas automáticos de reconocimiento del habla.
[06:31.000 --> 06:32.000]  ¿Por qué?
[06:32.000 --> 06:36.480]  Pues justamente para evitar que Whisper aprendiera también aquellos defectos, aquellos vicios
[06:36.480 --> 06:40.000]  que los otros sistemas automáticos también pudieran tener.
[06:40.000 --> 06:44.600]  Dicho esto, ahora que estamos hablando de Whisper y de YouTube, hay una teoría que
[06:44.600 --> 06:48.520]  quiero contaros que me parece muy interesante, no es nada que esté confirmado, pero que
[06:48.520 --> 06:53.560]  podría explicar la razón de existir de esta herramienta y que podría tener cierta relación
[06:53.560 --> 06:55.760]  con un futuro GPT-4.
[06:55.760 --> 06:59.720]  Esta es una idea que escuché en el canal del doctor Alan Thompson y que dice que en
[06:59.720 --> 07:05.600]  un futuro próximo, donde GPT-4 pueda empezar a entrenar, Whisper podría ofrecer al sistema
[07:05.600 --> 07:09.800]  una enorme fuente de datos con la que sistemas anteriores no habían contado.
[07:09.800 --> 07:14.640]  Pensemos que un sistema como GPT-3 se ha entrenado con un montón de artículos de Wikipedia,
[07:14.640 --> 07:19.120]  de libros, de foros, de conversaciones de Internet, pero nunca ha podido acceder a toda
[07:19.120 --> 07:23.640]  esa fuente hablada que puede estar en bases de datos como YouTube.
[07:23.640 --> 07:28.240]  Una herramienta como Whisper podría ser utilizada para barrer por completo a YouTube, transcribir
[07:28.240 --> 07:33.200]  muchos de sus audios y obtener, desbloquear una nueva fuente de datos que antes no habría
[07:33.200 --> 07:37.400]  sido posible utilizar para entrenar a un futuro modelo del lenguaje.
[07:37.400 --> 07:41.560]  Este es el enorme valor que tiene una herramienta como Whisper y que creo que hace tan interesante
[07:41.560 --> 07:42.560]  a esta tecnología.
[07:42.560 --> 07:47.680]  No, no resuelve una tarea que sea espectacular, como generar imágenes o generar vídeo, pero
[07:47.680 --> 07:52.280]  resuelve una tarea muy útil y casi la resuelve hasta la perfección.
[07:52.280 --> 07:57.640]  Ojo, digo casi, no es perfecta, a veces algunas palabras se equivocan evidentemente y no cubre
[07:57.640 --> 08:02.200]  todos los lenguajes que existen en el planeta Tierra y bueno, por buscar alguna limitación
[08:02.200 --> 08:07.320]  frente a otras herramientas comerciales, pues tampoco funciona en tiempo real todavía.
[08:07.320 --> 08:11.280]  Procesar el audio dependiendo de la longitud te puede llevar unos cuantos segundos, a veces
[08:11.280 --> 08:17.080]  algún minuto, pero es una herramienta sólida, es madura, es útil y además open source,
[08:17.080 --> 08:21.040]  permitiendo que ahora cualquiera pueda acceder a una herramienta profesional de transcripción
[08:21.040 --> 08:25.160]  y traducción de texto mejor que cualquier alternativa gratis.
[08:25.160 --> 08:26.160]  ¿Qué?
[08:26.160 --> 08:28.600]  Ah, que también vosotros queréis acceder a esta herramienta.
[08:28.600 --> 08:32.720]  Bueno, venga va, os preparo un tutorial facilito para que todos podáis utilizarlo.
[08:32.720 --> 08:37.640]  Vamos a hacerlo en Google Colab, pero antes y aprovechando que estamos hablando de programación,
[08:37.640 --> 08:41.880]  de desarrollo, de innovación, dejadme que os recuerde que quedan muy poquitos días
[08:41.880 --> 08:46.880]  para que se celebre el Samsung Dev Day, que es el evento tecnológico que celebra cada
[08:46.880 --> 08:51.760]  año la comunidad de Samsung Dev Spain, que es la comunidad oficial de Samsung para desarrolladores
[08:51.760 --> 08:52.840]  españoles.
[08:52.840 --> 08:55.560]  Este será un evento gratuito que no os podéis perder.
[08:55.560 --> 09:00.640]  Si estáis en Madrid podéis asistir presencialmente el día 16 de noviembre en el claustro de
[09:00.640 --> 09:04.840]  los Jerónimos del Museo del Prado y si no, pues podéis conectaros online a través de
[09:04.840 --> 09:05.840]  su streaming.
[09:05.840 --> 09:09.760]  Pero si, hay que registrarse, yo tuve la suerte el año pasado de poder participar con una
[09:09.760 --> 09:14.280]  ponencia sobre generación de código con inteligencia artificial y la experiencia fue
[09:14.280 --> 09:15.280]  genial.
[09:15.280 --> 09:18.800]  Así que ya lo veis, será un evento cargado de charlas geniales, hablando de tecnología,
[09:18.800 --> 09:23.280]  de innovación, de aplicaciones y además va a estar presentado por mi dudev, que seguramente
[09:23.280 --> 09:26.560]  muchos de vosotros le conozcáis, así que no os lo podéis perder.
[09:26.560 --> 09:30.320]  Os voy a dejar abajo en la cajita de descripción un enlace a la página web de Samsung Dev
[09:30.320 --> 09:35.160]  Spain, donde vais a encontrar toda la información respecto a la agenda donde registraros y un
[09:35.160 --> 09:37.040]  montón de recursos más.
[09:37.040 --> 09:38.720]  Nos vemos el 16 de noviembre.
[09:38.720 --> 09:43.400]  Pues vamos a ver cómo podemos utilizar Whisper nosotros en nuestro propio código.
[09:43.400 --> 09:47.240]  Para esto vamos a utilizar Google Colab, ya sabéis que Google aquí nos está cediendo
[09:47.240 --> 09:52.080]  una máquina virtual gratuita que podemos utilizar y vamos a verificar siempre que tengamos
[09:52.080 --> 09:56.560]  activado el tipo de entorno con aceleración por hardware GPU, vale, vamos a darle aquí
[09:56.560 --> 10:01.320]  GPU, vamos a darle a guardar y ahora el primer paso será instalar a Whisper.
[10:01.320 --> 10:05.600]  Para ello vamos a usar estos dos comandos de aquí, a instalar, esto lo podéis encontrar
[10:05.600 --> 10:11.160]  en el propio repositorio de GitHub de Whisper, os voy a dejar abajo en la cajita de descripción
[10:11.160 --> 10:14.160]  estos comandos, le damos a ejecutar y dejamos que se instale.
[10:14.160 --> 10:17.880]  Una vez instalado vamos a subir algún audio que queramos transcribir, yo en este caso
[10:17.880 --> 10:21.920]  voy a probar con la canción de Rosalía de Chicken Teriyaki, vamos a colocarla para acá,
[10:21.920 --> 10:26.800]  la arrastramos y ahora el siguiente paso pues vamos a coger aquí y vamos a poner el comando
[10:26.800 --> 10:31.640]  necesario para poder ejecutarlo, vamos a darle aquí a song.mp3, se llama el archivo que
[10:31.640 --> 10:37.680]  hemos subido, vale, song.mp3, la tarea va a ser pues transcribir el tamaño del modelo,
[10:37.680 --> 10:42.560]  hay diferentes tamaños según si quieres más velocidad a la hora de hacer la inferencia
[10:42.560 --> 10:46.920]  o si quieres más precisión en los resultados, yo por lo general trabajo con el modelo Medium
[10:46.920 --> 10:50.600]  que es el que me da buenos resultados, hay modelos mayores, hay modelos menores, probad
[10:50.600 --> 10:55.360]  y en este caso pues simplemente donde vamos a colocar el archivo de salida, ejecutamos
[10:55.360 --> 11:00.040]  y ya está, ya está, no hay que hacer nada más, vale, ya estamos utilizando Whisper,
[11:00.040 --> 11:03.660]  la primera vez tardará un poco porque tiene que descargar el modelo pero a partir de este
[11:03.660 --> 11:08.520]  momento podéis utilizar este sistema para transcribir cualquier audio que queráis,
[11:08.520 --> 11:13.640]  mola, vale, vemos que en este caso ha detectado que el idioma es español, ha hecho la inferencia
[11:13.640 --> 11:16.800]  automática porque no le hemos dicho que vamos a transcribir del español, lo podéis hacer
[11:16.800 --> 11:20.960]  si queréis y cuando ya está ejecutada esta celda pues podemos venirnos para acá, vemos
[11:20.960 --> 11:26.400]  que se ha generado la carpeta Audio Transcription y aquí tenemos las diferentes opciones, podemos
[11:26.400 --> 11:32.360]  abrir el sound.txt y aquí abrimos el archivo, vemos que pues tenemos toda la canción perfectamente
[11:32.360 --> 11:37.000]  transcrita que en este caso siendo la Rosalía pues tiene más mérito y en vez de querer
[11:37.000 --> 11:41.680]  hacer la transcripción, quisierais hacer la traducción, es decir convertir vuestra
[11:41.680 --> 11:45.640]  voz, vuestro audio al inglés, pues lo único que tenéis que hacer es cambiar aquí la
[11:45.640 --> 11:51.480]  tarea por Translate y en este caso Whisper trabajará para traducir aquello que ha transcrito.
[11:51.480 --> 11:54.880]  En este caso si os dais cuenta el comando que hemos utilizado ha sido el de consola
[11:54.880 --> 11:58.480]  pero a lo mejor queréis utilizar Whisper dentro de vuestro código, entonces también
[11:58.480 --> 12:02.000]  tenéis la opción de trabajar con la propia librería de Whisper, es simplemente esta
[12:02.000 --> 12:05.960]  línea de código de aquí, lo importamos, cargamos el modelo que queramos, aquí pues
[12:05.960 --> 12:10.960]  yo cargaría el modelo Medium que es el que como digo funciona mejor para mi caso y con
[12:10.960 --> 12:17.520]  el modelo cargado luego aquí llamamos a model.transcribe, vamos a poner aquí song.mp3, le damos a ejecutar
[12:17.520 --> 12:20.880]  y en cuestión de unos segundos pues ya tendremos de nuevo nuestra transcripción.
[12:20.880 --> 12:24.520]  Y aquí lo tenemos, la Rosalía, rosa sin tarjeta, se la mando a tu gata, te la tengo
[12:24.520 --> 12:27.600]  con ruleta, no hizo falta serenata, pues ok.
[12:27.600 --> 12:31.480]  Igualmente para haceros la vida más fácil he preparado un notebook que podéis utilizar,
[12:31.480 --> 12:35.000]  está abajo en la cajita de descripción, donde tenéis ya todo el código listo para
[12:35.000 --> 12:39.200]  empezar a trabajar, simplemente tenéis que entrar, comprobar que está la GPU activada,
[12:39.200 --> 12:43.080]  le damos a este botón de aquí para instalar pues todo lo necesario, aquí elegimos la
[12:43.080 --> 12:47.680]  tarea que queremos hacer, pues si es transcribir a cualquier idioma o traducir al inglés
[12:47.680 --> 12:48.800]  y le damos a ejecutar.
[12:48.800 --> 12:53.520]  En este caso la celda está preparada para que en el momento en el que empieces a ejecutarla
[12:53.520 --> 12:57.080]  está grabando ahora mismo tu micrófono, es decir ahora mismo estaríamos generando
[12:57.080 --> 13:00.960]  un archivo de audio que luego vamos a utilizar para transcribir con Whisper, esto es por
[13:00.960 --> 13:05.480]  si queréis hacer una transcripción en tiempo real de cualquier clase o cualquier cosa
[13:05.480 --> 13:06.480]  que necesitéis.
[13:06.480 --> 13:10.800]  Vamos a darle a parar, le damos a este botón y en un momento tenemos el resultado de lo
[13:10.800 --> 13:12.520]  que hemos dicho.
[13:12.520 --> 13:16.800]  Igualmente luego abajo os añado los dos comandos necesarios para poder transcribir o traducir
[13:16.800 --> 13:19.240]  el audio que vosotros subáis.
[13:19.240 --> 13:22.760]  Por último también tenéis que saber que si queréis algo más sencillo pues hay páginas
[13:22.760 --> 13:27.240]  web donde podéis probar este sistema pues subiendo vuestros propios audios o grabando
[13:27.240 --> 13:28.240]  desde el micrófono.
[13:28.240 --> 13:32.960]  Y esto sería, 2022 se está quedando la verdad que un año espectacular en cuanto al número
[13:32.960 --> 13:37.360]  de juguetes neuronales que están llegando a nuestras manos para construir un montón
[13:37.360 --> 13:39.320]  de herramientas y para poder toquetearlos.
[13:39.320 --> 13:41.640]  Ahora os toca a vosotros, ¿qué podéis hacer con esto?
[13:41.640 --> 13:45.080]  Pues podéis construir un montón de cosas súper interesantes, podéis conectar por
[13:45.080 --> 13:49.960]  ejemplo Whisper con Stable Diffusion para que a viva voz tú le puedas pedir que te
[13:49.960 --> 13:54.040]  genere un cuadro o podéis por ejemplo coger todas vuestras clases en la universidad o
[13:54.040 --> 13:58.960]  todas las reuniones de trabajo, transcribirlas, crear un enorme banco de transcripciones y
[13:58.960 --> 14:03.680]  luego con la API de GPT-3 hacer un chatbot que te permita consultar, hacer preguntas
[14:03.680 --> 14:06.160]  y respuestas sobre toda esa fuente de información.
[14:06.160 --> 14:10.040]  Por ejemplo algo que yo quiero hacer es coger pues todos los vídeos de mi canal de YouTube
[14:10.040 --> 14:14.640]  y transcribirlo, generar subtítulos de buena calidad tanto en español como en inglés
[14:14.640 --> 14:18.920]  y poder hacer estadísticas y consultas de cuántas veces he dicho por ejemplo la palabra
[14:18.920 --> 14:19.920]  Machine Learning.
[14:19.920 --> 14:23.360]  Hay un montón de aplicaciones que podéis empezar a construir, que podéis empezar a
[14:23.360 --> 14:27.160]  crear combinando todas estas tecnologías.
[14:27.160 --> 14:29.880]  Tenía un perro ladrando de fondo que me estaba molestando bastante.
[14:29.880 --> 14:34.080]  Bueno, lo que os decía, que podéis crear un montón de cosas y hay mucho por hacer.
[14:34.080 --> 14:37.560]  Desde aquí, desde este canal vamos a seguir haciendo experimentos con esta tecnología,
[14:37.560 --> 14:42.320]  voy a seguir trayendo nuevas herramientas así que si no lo has hecho todavía suscríbete,
[14:42.320 --> 14:46.000]  dale a la campanita para que te lleguen siempre las notificaciones de que hay vídeo nuevo
[14:46.000 --> 14:50.440]  y si quieres apoyar todo este contenido ya sabéis que podéis hacerlo a través de Patreon
[14:50.440 --> 14:52.080]  abajo en la cajita de descripción.
[14:52.080 --> 14:55.080]  Tenéis un par de vídeos por aquí que son súper interesantes, no sé cuáles son pero
[14:55.080 --> 14:58.960]  son súper interesantes, echadle un ojo y nos vemos con más inteligencia artificial
[14:58.960 --> 15:26.280]  chicos, chicas, en el próximo vídeo.
```

**output_formats**: `txt,vtt,srt`

```
Writing results...

audio_transcription/Whisper-Example.txt
audio_transcription/Whisper-Example.vtt
audio_transcription/Whisper-Example.srt
```

[audio_transcription/Whisper-Example.txt](audio_transcription/Whisper-Example.txt)

[audio_transcription/Whisper-Example.vtt](audio_transcription/Whisper-Example.vtt)

[audio_transcription/Whisper-Example.srt](audio_transcription/Whisper-Example.srt)

**deepl_target_language**: `English (British)`

**deepl_formality**: `default`

**deepl_coherence_preference**: `Share context between lines`

```
Whisper-Example.3gp

DeepL: Translate results from Spanish [ES] to English (British) [EN-GB]

[00:00.000 --> 00:06.040] 2022 will be remembered as the year of Stable Diffusion, of Dalí 2, of incredible models
[00:06.040 --> 00:10.160] text generators like Palm or code generators like AlphaCode.
[00:10.160 --> 00:13.920] And yet, chatting last month with Andrés Torrubia, he told me that the
[00:13.920 --> 00:18.120] most interesting thing he had seen this year was an artificial intelligence that came
[00:18.120 --> 00:21.880] from the OpenAI lab, an AI called Whisper.
[00:21.880 --> 00:26.880] What do you think is the most impressive thing that has come out this year?
[00:26.880 --> 00:31.800] Well, curiously, look, curiously, so far Whisper, I think.
[00:31.800 --> 00:32.800] Do you know why?
[00:32.800 --> 00:33.800] Curious, eh.
[00:33.800 --> 00:39.760] What impresses me about Whisper is that Whisper works, it's like, for me, Whisper, if it were
[00:39.760 --> 00:46.880] the autonomous car, would be the first self-driving car in dictation, in other words, it's the first one that looks like
[00:46.880 --> 00:47.880] a person.
[00:47.880 --> 00:51.000] Well, but in order for you to first understand what Whisper is, I am going to ask you to
[00:51.000 --> 00:53.120] do the following exercise.
[00:53.120 --> 00:57.800] I'm going to play you an audio in English and your task is to transcribe each of the words
[00:57.800 --> 00:59.600] you hear.
[00:59.600 --> 01:00.600] Are you ready?
[01:00.600 --> 01:02.600] Three, two, one.
[01:19.800 --> 01:21.280] Did you understand anything?
[01:21.280 --> 01:22.760] Yeah, me neither.
[01:22.760 --> 01:28.160] Well, to this artificial intelligence, this is the perfect transcription it has achieved.
[01:28.160 --> 01:29.400] How's your Korean?
[01:29.400 --> 01:33.680] Well, it's no problem for Whisper either and it can also transcribe this audio in
[01:33.680 --> 01:35.520] perfect English.
[01:44.440 --> 01:46.080] And well, it understands me too.
[01:46.080 --> 01:50.040] What you are seeing on the screen now is the speech to text that Whisper gets when
[01:50.040 --> 01:52.680] passes it the audio track you are listening to.
[01:52.680 --> 01:57.440] Look closely, not only does it get an almost perfect transcription, understanding even specific words
[01:57.440 --> 02:02.760] like Whisper or speech to text, but it is also able to generate full stops, commas
[02:02.760 --> 02:06.560] and other punctuation marks that many other commercial models of speech recognition
[02:06.560 --> 02:08.360] usually struggle to do.
[02:08.360 --> 02:10.720] And this is very interesting.
[02:10.720 --> 02:12.960] Well, not this, but Whisper.
[02:12.960 --> 02:18.160] Whisper in general has many interesting things and the first interesting thing is the context
[02:18.160 --> 02:20.120] in which this tool appears.
[02:20.120 --> 02:23.640] After a year of incredible achievements by the Artificial Intelligence Lab
[02:23.640 --> 02:29.680] of OpenAI, suddenly out of nowhere a collaborative initiative like Stability.ai
[02:29.680 --> 02:34.320] emerges, which in September takes as a flag to make open source many of the technologies that
[02:34.320 --> 02:40.240] OpenAI on its part has decided to keep to itself and share only under paid
[02:40.240 --> 02:41.240] services.
[02:41.240 --> 02:46.360] For me this is not a problem either, since in the end OpenAI as a company has
[02:46.360 --> 02:50.720] to pay its bills and at least it is giving us a way to access these powerful
[02:50.720 --> 02:52.360] artificial intelligences.
[02:52.360 --> 02:53.920] Learn Google.
[02:53.920 --> 02:57.880] But of course, a new kid comes to town and starts giving away candy to the
[02:57.880 --> 03:01.920] children and suddenly the popular kid starts to be displaced.
[03:01.920 --> 03:07.760] And at that precise moment OpenAI comes out of nowhere and gives us Whisper for the benefit
[03:07.760 --> 03:08.760] of all.
[03:08.760 --> 03:13.580] Because yes, friends, this is open source, I know you love to hear these words.
[03:13.580 --> 03:17.160] At the end of the video I will show a mini tutorial so you can see how easy it is to use
[03:17.160 --> 03:21.000] this tool and I will also share a notebook to make it super simple for
[03:21.000 --> 03:22.000] you.
[03:22.000 --> 03:25.800] And this is what makes Whisper a super interesting tool, but it is not the only thing.
[03:25.800 --> 03:29.800] And this is where one of the things that has caught my attention the most is that Whisper
[03:29.800 --> 03:34.440] is not a complex system that they have designed to process audio like they have never
[03:34.440 --> 03:38.640] done before or a super complex system with a bunch of processing modules.
[03:38.640 --> 03:45.840] No, Whisper is this right here, a transformer neural network of 2017, it has
[03:45.840 --> 03:47.920] no changes, nothing new.
[03:47.920 --> 03:51.280] It is an architecture that we are all already familiar with.
[03:51.280 --> 03:55.800] So, if this is so, why didn't a technology like Whisper already exist?
[03:55.800 --> 04:00.800] Well, the key that makes Whisper so powerful is in the data and in how
[04:00.800 --> 04:02.920] has structured its training.
[04:02.920 --> 04:09.040] To train it, OpenAI has used no less than 680,000 hours of audio with its corresponding text
[04:09.040 --> 04:12.360] a brutality.
[04:12.360 --> 04:17.200] And if you calculate 680,000 hours and start playing them now, you would end up
[04:17.200 --> 04:19.880] listening to it in 77 years' time.
[04:19.880 --> 04:24.160] You could be sure that at some point in the sky you would see Halley's comet fly.
[04:24.160 --> 04:28.560] But what's more, a very interesting thing is that these audios come in multiple languages,
[04:28.560 --> 04:32.200] allowing us to train a model that is multilingual, that can understand us
[04:32.200 --> 04:36.560] if we speak to it in Spanish, English, Korean, whatever.
[04:36.560 --> 04:38.240] But that's not all.
[04:38.240 --> 04:43.720] And Whisper, as well as being a multilingual system, is also a multitasking system.
[04:43.720 --> 04:47.520] This is a trend that, as we saw in the video on Gato, is becoming more and more frequent in the world of deep
[04:47.520 --> 04:49.760] learning.
[04:49.760 --> 04:54.680] Not to train artificial intelligence for a single task, but to train it for several different
[04:54.680 --> 04:59.560] thus making its learning much more solid and robust.
[04:59.560 --> 05:04.560] As we have seen, Whisper can take audio in English and transcribe it into English, or
[05:04.560 --> 05:06.960] audio in Korean and transcribe it into Korean.
[05:06.960 --> 05:11.200] But the same model can also identify which language is being spoken, or act
[05:11.200 --> 05:15.360] as a voice detector to classify when a piece of audio is not
[05:15.360 --> 05:16.360] listening to a person.
[05:16.360 --> 05:20.960] Or, the most interesting task of all, you can speak
[05:20.960 --> 05:25.720] to Whisper in any language and it will automatically transcribe it into English for you.
[05:25.720 --> 05:29.800] And in this case I can't tell you why, but I find this functionality
[05:29.800 --> 05:30.800] fascinating.
[05:30.800 --> 05:32.880] It doesn't seem to offer us anything new either, does it?
[05:32.880 --> 05:37.560] In the end you can take the text generated by any text transcriber in your language
[05:37.560 --> 05:39.520] and pass it through a translator.
[05:39.520 --> 05:43.520] But in this case I find it fascinating to see how something as simple as a single
[05:43.520 --> 05:47.880] deep learning model allows you to speak to it in any language and it generates the text
[05:47.880 --> 05:51.520] in English without having to combine any kind of tools.
[05:51.520 --> 05:53.400] It's super simple.
[05:53.400 --> 05:56.360] And the data that we mentioned before is also super interesting.
[05:56.360 --> 06:00.480] Because my first intuition here is that OpenAI, in the search for a massive dataset
[06:00.480 --> 06:05.280] of these 680,000 hours of audio that had a text transcription to be able to do
[06:05.280 --> 06:09.800] this supervised learning, had possibly turned to one of the biggest sources
[06:09.800 --> 06:12.520] that we can find on the Internet, which is YouTube.
[06:12.520 --> 06:16.960] In the end you know that all YouTube videos have automatically generated subtitles.
[06:16.960 --> 06:17.960] Well no.
[06:17.960 --> 06:22.800] This is precisely what OpenAI emphasises in its paper to explain that they have done
[06:22.800 --> 06:28.200] a filtering process to eliminate from the dataset any text generated by
[06:28.200 --> 06:31.000] automatic speech recognition systems.
[06:31.000 --> 06:32.000] Why?
[06:32.000 --> 06:36.480] Well, precisely to prevent Whisper from learning also those defects, those vices
[06:36.480 --> 06:40.000] that the other automatic systems might also have.
[06:40.000 --> 06:44.600] Having said that, now that we are talking about Whisper and YouTube, there is a theory that
[06:44.600 --> 06:48.520] would like to tell you about that I find very interesting, it is nothing that is confirmed, but that
[06:48.520 --> 06:53.560] could explain the reason for the existence of this tool and that could have a certain relationship
[06:53.560 --> 06:55.760] with a future GPT-4.
[06:55.760 --> 06:59.720] This is an idea I heard on Dr Alan Thompson's channel that says that at
[06:59.720 --> 07:05.600] in the near future, where GPT-4 can start training, Whisper could offer the
[07:05.600 --> 07:09.800] system a huge source of data that previous systems have not had.
[07:09.800 --> 07:14.640] Let's think that a system like GPT-3 has been trained with a lot of Wikipedia articles,
[07:14.640 --> 07:19.120] from books, from forums, from Internet conversations, but it has never been able to access all
[07:19.120 --> 07:23.640] that spoken source that may be in databases like YouTube.
[07:23.640 --> 07:28.240] A tool like Whisper could be used to completely sweep YouTube, transcribe
[07:28.240 --> 07:33.200] many of its audios and obtain, unlock a new source of data that previously would not have
[07:33.200 --> 07:37.400] been possible to use to train a future language model.
[07:37.400 --> 07:41.560] This is the enormous value of a tool like Whisper that I think makes
[07:41.560 --> 07:42.560] so interesting.
[07:42.560 --> 07:47.680] No, it doesn't solve a task that is spectacular, like generating images or generating video, but
[07:47.680 --> 07:52.280] solves a very useful task and almost solves it to perfection.
[07:52.280 --> 07:57.640] I say almost, it is not perfect, sometimes some words are obviously wrong and it does not cover
[07:57.640 --> 08:02.200] all the languages that exist on planet Earth and, well, to look for a limitation
[08:02.200 --> 08:07.320] compared to other commercial tools, it does not work in real time yet.
[08:07.320 --> 08:11.280] Processing the audio depending on the length can take a few seconds, sometimes
[08:11.280 --> 08:17.080] a few minutes, but it is a solid tool, it is mature, it is useful and it is open source,
[08:17.080 --> 08:21.040] allowing anyone to have access to a professional transcription tool
[08:21.040 --> 08:25.160] and text translation better than any free alternative.
[08:25.160 --> 08:26.160] What?
[08:26.160 --> 08:28.600] Ah, that you also want to have access to this tool.
[08:28.600 --> 08:32.720] Well, come on, I'll prepare an easy tutorial so you can all use it.
[08:32.720 --> 08:37.640] We're going to do it on Google Colab, but first and since we're talking about programming,
[08:37.640 --> 08:41.880] development, innovation, let me remind you that there are very few days left
[08:41.880 --> 08:46.880] to celebrate the Samsung Dev Day, which is the technological event held every
[08:46.880 --> 08:51.760] year by the Samsung Dev Spain community, which is the official Samsung community for developers
[08:51.760 --> 08:52.840] Spanish.
[08:52.840 --> 08:55.560] This will be a free event that you can't miss.
[08:55.560 --> 09:00.640] If you are in Madrid you can attend in person on November 16th in the cloister of
[09:00.640 --> 09:04.840] los Jerónimos of the Prado Museum and if not, you can connect online through
[09:04.840 --> 09:05.840] its streaming.
[09:05.840 --> 09:09.760] But yes, you have to register, I was lucky enough to participate last year with a
[09:09.760 --> 09:14.280] presentation on code generation with artificial intelligence and the experience was
[09:14.280 --> 09:15.280] great.
[09:15.280 --> 09:18.800] So you can see, it will be an event full of great talks, talking about technology,
[09:18.800 --> 09:23.280] innovation, applications and it will also be presented by my dudev, who probably
[09:23.280 --> 09:26.560] many of you know, so you can not miss it.
[09:26.560 --> 09:30.320] I'm going to leave below in the description box a link to the Samsung Dev website
[09:30.320 --> 09:35.160] Spain, where you will find all the information regarding the agenda where to register and a
[09:35.160 --> 09:37.040] lot of resources.
[09:37.040 --> 09:38.720] See you on November 16.
[09:38.720 --> 09:43.400] So let's see how we can use Whisper ourselves in our own code.
[09:43.400 --> 09:47.240] For this we will use Google Colab, you know that Google here is giving us
[09:47.240 --> 09:52.080] a free virtual machine that we can use and we will verify that we have
[09:52.080 --> 09:56.560] enabled the type of environment with hardware acceleration GPU, okay, we will give here
[09:56.560 --> 10:01.320] GPU, we will give save and now the first step will be to install Whisper.
[10:01.320 --> 10:05.600] To do this we're going to use these two commands here, to install, you can find
[10:05.600 --> 10:11.160] in the Whisper GitHub repository, I'm going to leave these commands below in the description box
[10:11.160 --> 10:14.160] hit run and let it install.
[10:14.160 --> 10:17.880] Once installed we are going to upload some audio that we want to transcribe, in this case
[10:17.880 --> 10:21.920] I am going to try with the song of Rosalía de Chicken Teriyaki, we are going to place it here,
[10:21.920 --> 10:26.800] we drag it and now the next step because we are going to take here and we are going to put the command
[10:26.800 --> 10:31.640] necessary to be able to execute it, we are going to give here to song.mp3, it is called the file that
[10:31.640 --> 10:37.680] we have uploaded, ok, song.mp3, the task is going to be to transcribe the size of the model,
[10:37.680 --> 10:42.560] there are different sizes depending on whether you want more speed when doing the inference
[10:42.560 --> 10:46.920] or if you want more precision in the results, I generally work with the Medium model
[10:46.920 --> 10:50.600] which is the one that gives me good results, there are bigger models, there are smaller models, try
[10:50.600 --> 10:55.360] and in this case simply where we are going to place the output file, we execute
[10:55.360 --> 11:00.040] and that's it, that's it, we don't have to do anything else, OK, we are already using Whisper,
[11:00.040 --> 11:03.660] the first time it will take a little while because it has to download the model but from this
[11:03.660 --> 11:08.520] moment on you can use this system to transcribe any audio you want,
[11:08.520 --> 11:13.640] cool, ok, we can see that in this case it has detected that the language is Spanish, it has made the inference
[11:13.640 --> 11:16.800] automatically because we have not told it that we are going to transcribe from Spanish, you can do it
[11:16.800 --> 11:20.960] if you want and when this cell is already executed we can come here, we see
[11:20.960 --> 11:26.400] that the Audio Transcription folder has been generated and here we have the different options, we can
[11:26.400 --> 11:32.360] open the sound.txt and here we open the file, we see that we have the whole song perfectly
[11:32.360 --> 11:37.000] transcribed and in this case being Rosalía it has more merit and instead of wanting to
[11:37.000 --> 11:41.680] do the transcription, you would like to do the translation, that is to say convert your
[11:41.680 --> 11:45.640] voice, your audio to English, all you have to do is change here the
[11:45.640 --> 11:51.480] task to Translate and in this case Whisper will work to translate what it has transcribed.
[11:51.480 --> 11:54.880] In this case if you notice the command that we have used has been the one of console
[11:54.880 --> 11:58.480] but maybe you want to use Whisper inside your code, then also
[11:58.480 --> 12:02.000] you have the option to work with the own library of Whisper, it is simply this
[12:02.000 --> 12:05.960] line of code of here, we import it, we load the model that we want, here then
[12:05.960 --> 12:10.960] I would load the model Medium that is the one that as I say works better for my case and with
[12:10.960 --> 12:17.520] the loaded model then here we call model.transcribe, we are going to put here song.mp3, we give to execute
[12:17.520 --> 12:20.880] and in a matter of seconds we will have our transcription again.
[12:20.880 --> 12:24.520] And here we have it, the Rosalía, rose without card, I send it to your cat, I have it to you
[12:24.520 --> 12:27.600] with roulette, it was not necessary serenade, ok.
[12:27.600 --> 12:31.480] Also to make your life easier I have prepared a notebook that you can use,
[12:31.480 --> 12:35.000] is below in the description box, where you have all the code ready to
[12:35.000 --> 12:39.200] start working, you just have to enter, check that the GPU is activated,
[12:39.200 --> 12:43.080] we click this button here to install everything you need, here we choose the
[12:43.080 --> 12:47.680] task we want to do, if it is transcribe to any language or translate to English
[12:47.680 --> 12:48.800] and we click run.
[12:48.800 --> 12:53.520] In this case the cell is prepared so that at the moment you start to execute it
[12:53.520 --> 12:57.080] is recording right now your microphone, that is to say right now we would be generating
[12:57.080 --> 13:00.960] an audio file that later we are going to use to transcribe with Whisper, this is for
[13:00.960 --> 13:05.480] if you want to make a transcription in real time of any class or any thing
[13:05.480 --> 13:06.480] that you need.
[13:06.480 --> 13:10.800] We are going to give him to stop, we give him to this button and in a moment we have the result of the
[13:10.800 --> 13:12.520] that we have said.
[13:12.520 --> 13:16.800] Equally then below I add you the two necessary commands to be able to transcribe or to translate
[13:16.800 --> 13:19.240] the audio that you upload.
[13:19.240 --> 13:22.760] Finally, you should also know that if you want something simpler, there are
[13:22.760 --> 13:27.240] web pages where you can try this system by uploading your own audio or recording
[13:27.240 --> 13:28.240] from the microphone.
[13:28.240 --> 13:32.960] And that's it, 2022 is shaping up to be a spectacular year in terms of the number
[13:32.960 --> 13:37.360] of neural toys that are coming into our hands to build a lot
[13:37.360 --> 13:39.320] of tools and to be able to play them.
[13:39.320 --> 13:41.640] Now it's your turn, what can you do with these?
[13:41.640 --> 13:45.080] Well, you can build a lot of super interesting things, you can connect for example
[13:45.080 --> 13:49.960] Whisper with Stable Diffusion so that you can ask
[13:49.960 --> 13:54.040] to generate a chart or you can for example take all your university classes or
[13:54.040 --> 13:58.960] all your work meetings, transcribe them, create a huge bank of transcripts and
[13:58.960 --> 14:03.680] then with the GPT-3 API make a chatbot that allows you to consult, ask questions
[14:03.680 --> 14:06.160] and answers about all that source of information.
[14:06.160 --> 14:10.040] For example, something I want to do is to take all the videos from my YouTube channel
[14:10.040 --> 14:14.640] and transcribe them, generate good quality subtitles in both Spanish and English
[14:14.640 --> 14:18.920] and be able to make statistics and queries on how many times I have said the word
[14:18.920 --> 14:19.920] Machine Learning, for example.
[14:19.920 --> 14:23.360] There are a lot of applications that you can start to build, that you can start to
[14:23.360 --> 14:27.160] create by combining all these technologies.
[14:27.160 --> 14:29.880] I had a dog barking in the background that was bothering me a lot.
[14:29.880 --> 14:34.080] Well, what I was saying, you can create a lot of things and there is a lot to do.
[14:34.080 --> 14:37.560] From here, from this channel we are going to keep experimenting with this technology,
[14:37.560 --> 14:42.320] I will keep bringing you new tools so if you haven't subscribed yet,
[14:42.320 --> 14:46.000] click on the little bell so you always get notifications of new videos
[14:46.000 --> 14:50.440] and if you want to support all this content you know you can do it through Patreon
[14:50.440 --> 14:52.080] below in the description box.
[14:52.080 --> 14:55.080] You have a couple of videos here that are super interesting, I don't know what they are but
[14:55.080 --> 14:58.960] are super interesting, take a look at them and see you with more artificial intelligence
[14:58.960 --> 15:26.280] guys, girls, in the next video.

DeepL: Character usage: 16558 / 500000 (3.31%)

Writing translated results...

audio_transcription/Whisper-Example_English (British).txt
audio_transcription/Whisper-Example_English (British).vtt
audio_transcription/Whisper-Example_English (British).srt
```

[audio_transcription/Whisper-Example_English (British).txt](<audio_transcription/Whisper-Example_English%20(British).txt>)

[audio_transcription/Whisper-Example_English (British).vtt](<audio_transcription/Whisper-Example_English%20(British).vtt>)

[audio_transcription/Whisper-Example_English (British).srt](<audio_transcription/Whisper-Example_English%20(British).srt>)

### About translation coherence

When translating to another language using **deepl_coherence_preference** `Share context between lines` to have a high quality translation, some words may change their order in the sentences according to the language's grammar, and then translated sentences do not match exactly the original language timestamps.

If you do not like the previous output captions, you can try setting **deepl_coherence_preference** to `Translate each line independently`, in which sentences are translated independently, so the words are kept in the same sentences and timestamps as in the original language captions.
However, this results in an overall worse translation due to missing context in sentences that are split between different lines.

This is the output with this preference change:

**deepl_coherence_preference**: `Translate each line independently`

```
[00:00.000 --> 00:06.040] 2022 will be remembered as the year of Stable Diffusion, of Dali 2, of incredible models
[00:06.040 --> 00:10.160] text generators such as Palm or code generators such as AlphaCode.
[00:10.160 --> 00:13.920] And yet, chatting last month with Andrés Torrubia, he told me that the
[00:13.920 --> 00:18.120] most interesting thing I'd seen this year was an artificial intelligence that was coming
[00:18.120 --> 00:21.880] from the OpenAI lab, an AI called Whisper.
[00:21.880 --> 00:26.880] What do you think is the most impressive thing that has come out this year?
[00:26.880 --> 00:31.800] Well, oddly enough, look, oddly enough, so far Whisper, I think.
[00:31.800 --> 00:32.800] Do you know why?
[00:32.800 --> 00:33.800] Curious, eh.
[00:33.800 --> 00:39.760] What impresses me about Whisper is that Whisper works, it's like, for me, Whisper, if it were
[00:39.760 --> 00:46.880] the autonomous car, it would be the first self-driving car in the dictation, i.e. it is the first one that resembles
[00:46.880 --> 00:47.880] to a person.
[00:47.880 --> 00:51.000] Well, but in order for you to first understand what this Whisper thing is, I'm going to ask you to
[00:51.000 --> 00:53.120] do the following exercise.
[00:53.120 --> 00:57.800] I am going to play you an audio in English and your task is to transcribe each of the words
[00:57.800 --> 00:59.600] you are listening to.
[00:59.600 --> 01:00.600] Are you ready?
[01:00.600 --> 01:02.600] Three, two, one.
[01:19.800 --> 01:21.280] Have you understood anything?
[01:21.280 --> 01:22.760] Yeah, me neither.
[01:22.760 --> 01:28.160] Well, in the ears of this artificial intelligence, this is the perfect transcription it has achieved.
[01:28.160 --> 01:29.400] How is your Korean?
[01:29.400 --> 01:33.680] Well, it's no problem for Whisper either, and he can also transcribe this audio at
[01:33.680 --> 01:35.520] perfect English.
[01:44.440 --> 01:46.080] And well, he understands me too.
[01:46.080 --> 01:50.040] What you're seeing on the screen now is the speech to text that Whisper gets when it
[01:50.040 --> 01:52.680] I pass on the audio track you are listening to.
[01:52.680 --> 01:57.440] Look closely, not only does he get a near-perfect transcription, understanding even words
[01:57.440 --> 02:02.760] such as Whisper or speech to text, but it is also capable of generating full stops, commas
[02:02.760 --> 02:06.560] and other punctuation marks than many other commercial recognition models
[02:06.560 --> 02:08.360] of speech as he tends to choke on it.
[02:08.360 --> 02:10.720] And this is very interesting.
[02:10.720 --> 02:12.960] Well, not this, but Whisper.
[02:12.960 --> 02:18.160] Whisper in general has many interesting things and the first interesting thing is the context
[02:18.160 --> 02:20.120] in which this tool appears.
[02:20.120 --> 02:23.640] After a year of amazing achievements by the Artificial Intelligence Lab
[02:23.640 --> 02:29.680] OpenAI, suddenly out of the blue a collaborative initiative like Stability.ai
[02:29.680 --> 02:34.320] which in September takes up the banner of making open source many of the technologies that
[02:34.320 --> 02:40.240] OpenAI for its part has decided to keep to itself and share only under services
[02:40.240 --> 02:41.240] payment.
[02:41.240 --> 02:46.360] This is not a problem for me either, because in the end OpenAI as a company has
[02:46.360 --> 02:50.720] to pay their bills and at least it's giving us a way to access these powerful
[02:50.720 --> 02:52.360] artificial intelligences.
[02:52.360 --> 02:53.920] Learn Google.
[02:53.920 --> 02:57.880] But of course, a new little boy arrives in town and starts giving out sweets to the
[02:57.880 --> 03:01.920] children and all of a sudden the popular kid starts to be displaced.
[03:01.920 --> 03:07.760] And at that precise moment OpenAI comes out of nowhere and gives us Whisper for our benefit
[03:07.760 --> 03:08.760] of all.
[03:08.760 --> 03:13.580] Because yes, my friends, this is open source, and I know you love to hear these words.
[03:13.580 --> 03:17.160] At the end of the video I'm going to show you a mini tutorial so you can see how easy it is to use
[03:17.160 --> 03:21.000] this tool and I'm also going to share a notebook to make it super easy for you to
[03:21.000 --> 03:22.000] you.
[03:22.000 --> 03:25.800] And this is what makes Whisper a super interesting tool, but it is not the only thing.
[03:25.800 --> 03:29.800] And this is where one of the things that has caught my attention is that Whisper
[03:29.800 --> 03:34.440] is not a complex system that has been designed to process audio in a way that has never been done before
[03:34.440 --> 03:38.640] made or a super-complex system with a lot of processing modules.
[03:38.640 --> 03:45.840] No, Whisper is this right here, a transformer neural network from 2017, it doesn't have
[03:45.840 --> 03:47.920] no change, nothing new.
[03:47.920 --> 03:51.280] It is an architecture with which we are all familiar.
[03:51.280 --> 03:55.800] So, if this is the case, why didn't a technology like Whisper already exist?
[03:55.800 --> 04:00.800] Well, the key to what makes Whisper so powerful is in the data and how it has been used
[04:00.800 --> 04:02.920] structured their training.
[04:02.920 --> 04:09.040] To train him, OpenAI used no less than 680,000 hours of audio with its
[04:09.040 --> 04:12.360] corresponding text, a brutality.
[04:12.360 --> 04:17.200] And if you calculate 680,000 hours and start reproducing them now, you would end up with
[04:17.200 --> 04:19.880] to listen to it 77 years from now.
[04:19.880 --> 04:24.160] You could be sure that at some point in the sky you would see Halley's comet streaking across the sky.
[04:24.160 --> 04:28.560] But what's more, a very interesting thing is that these audios come in multiple languages,
[04:28.560 --> 04:32.200] allowing us to be able to train a model that is multilingual, that can understand us
[04:32.200 --> 04:36.560] whether we speak to him in Spanish, English, Korean, it doesn't matter.
[04:36.560 --> 04:38.240] But it doesn't stop there.
[04:38.240 --> 04:43.720] Whisper is not only a multilingual system, but also a multitasking system.
[04:43.720 --> 04:47.520] This is a trend that, as we saw in the video on Gato, in the world of deep
[04:47.520 --> 04:49.760] learning is becoming more and more frequent.
[04:49.760 --> 04:54.680] Do not train artificial intelligence for a single task, but train it for several tasks
[04:54.680 --> 04:59.560] different, thus making their learning much more solid and robust.
[04:59.560 --> 05:04.560] As we have seen, Whisper can take audios in English and transcribe them into English, or
[05:04.560 --> 05:06.960] audio in Korean and transcribe it into Korean.
[05:06.960 --> 05:11.200] But the same model can also identify which language is being spoken, or acted upon
[05:11.200 --> 05:15.360] as a speech detector to classify when a piece of audio is not being listened to
[05:15.360 --> 05:16.360] to a person.
[05:16.360 --> 05:20.960] Or also, the task that I find most interesting of all, that you can talk to him or her
[05:20.960 --> 05:25.720] to Whisper in any language and have it automatically transcribe it into English for you.
[05:25.720 --> 05:29.800] And in this case I can't tell you why, but for me this seems to me to be one of the most important functions
[05:29.800 --> 05:30.800] fascinating.
[05:30.800 --> 05:32.880] It doesn't seem to offer us anything new either, does it?
[05:32.880 --> 05:37.560] In the end you can take the text generated by any text transcriber in your language
[05:37.560 --> 05:39.520] and run it through a translator.
[05:39.520 --> 05:43.520] But in this case, I find it fascinating to see how something as simple as a single
[05:43.520 --> 05:47.880] deep learning model allows you to speak to it in any language and have it generate the text for you
[05:47.880 --> 05:51.520] in English without having to combine any tools.
[05:51.520 --> 05:53.400] It's super simple.
[05:53.400 --> 05:56.360] And the data we discussed earlier is also very interesting.
[05:56.360 --> 06:00.480] Because my first intuition here is that OpenAI, in the search for a massive dataset
[06:00.480 --> 06:05.280] of these 680,000 hours of audio to have a text transcription in order to be able to make
[06:05.280 --> 06:09.800] this supervised apprenticeship, as he had possibly gone to one of the largest sources of
[06:09.800 --> 06:12.520] that we can find on the Internet, which is YouTube.
[06:12.520 --> 06:16.960] In the end you know that all YouTube videos are automatically generated with subtitles.
[06:16.960 --> 06:17.960] Well, no.
[06:17.960 --> 06:22.800] This is precisely what OpenAI puts a lot of emphasis on in its paper to explain what they have done
[06:22.800 --> 06:28.200] a filtering process to remove from the dataset any text occurrences generated by
[06:28.200 --> 06:31.000] automatic speech recognition systems.
[06:31.000 --> 06:32.000] Why?
[06:32.000 --> 06:36.480] It was precisely to prevent Whisper from learning those defects, those vices, too
[06:36.480 --> 06:40.000] that other automatic systems may also have.
[06:40.000 --> 06:44.600] That said, now that we're talking about Whisper and YouTube, there is a theory that
[06:44.600 --> 06:48.520] I want to tell you that I think it's very interesting, it's nothing that is confirmed, but that
[06:48.520 --> 06:53.560] could explain the reason for the existence of this tool and that it could have a certain relationship with the
[06:53.560 --> 06:55.760] with a future GPT-4.
[06:55.760 --> 06:59.720] This is an idea I heard on Dr. Alan Thompson's channel, which says that in
[06:59.720 --> 07:05.600] the near future, where GPT-4 can begin training, Whisper could offer the system
[07:05.600 --> 07:09.800] a huge source of data that previous systems had not been able to count on.
[07:09.800 --> 07:14.640] Think of a system like GPT-3 as having been trained with a lot of Wikipedia articles,
[07:14.640 --> 07:19.120] of books, of forums, of Internet conversations, but he has never been able to access all of the
[07:19.120 --> 07:23.640] that spoken source that may be in databases such as YouTube.
[07:23.640 --> 07:28.240] A tool such as Whisper could be used to sweep YouTube completely, transcribe
[07:28.240 --> 07:33.200] many of their audios and get, unlock a new source of data that previously would not have
[07:33.200 --> 07:37.400] It has been possible to use it to train a future language model.
[07:37.400 --> 07:41.560] This is the enormous value of a tool like Whisper that I think makes it so interesting
[07:41.560 --> 07:42.560] to this technology.
[07:42.560 --> 07:47.680] No, it does not solve a task that is spectacular, such as generating images or generating video, but it does
[07:47.680 --> 07:52.280] solves a very useful task and almost solves it to perfection.
[07:52.280 --> 07:57.640] I say almost, it's not perfect, sometimes some words are obviously wrong and it doesn't cover it
[07:57.640 --> 08:02.200] all the languages that exist on planet Earth, and well, to look for some limitation
[08:02.200 --> 08:07.320] compared to other commercial tools, as it does not yet work in real time either.
[08:07.320 --> 08:11.280] Depending on the length of the audio it can take a few seconds to process it, sometimes
[08:11.280 --> 08:17.080] It's a solid tool, it's mature, it's useful and it's open source,
[08:17.080 --> 08:21.040] now allowing anyone to have access to a professional transcription tool
[08:21.040 --> 08:25.160] and text translation better than any free alternative.
[08:25.160 --> 08:26.160] What?
[08:26.160 --> 08:28.600] Oh, that you too would like to have access to this tool.
[08:28.600 --> 08:32.720] Well, come on, I'll prepare an easy tutorial for all of you to use.
[08:32.720 --> 08:37.640] We are going to do it in Google Colab, but first and taking advantage of the fact that we are talking about programming,
[08:37.640 --> 08:41.880] of development, of innovation, let me remind you that there are very few days left
[08:41.880 --> 08:46.880] for Samsung Dev Day, which is the technology event held every year to celebrate the Samsung
[08:46.880 --> 08:51.760] year the Samsung Dev Spain community, which is Samsung's official community for developers
[08:51.760 --> 08:52.840] Spanish.
[08:52.840 --> 08:55.560] This will be a free event not to be missed.
[08:55.560 --> 09:00.640] If you are in Madrid you can attend in person on 16th November at the cloister of
[09:00.640 --> 09:04.840] the Hieronymites of the Museo del Prado and if not, you can connect online at
[09:04.840 --> 09:05.840] its streaming.
[09:05.840 --> 09:09.760] But yes, you have to register, I was lucky enough to be able to participate last year with one of my own
[09:09.760 --> 09:14.280] presentation on code generation with artificial intelligence and the experience was
[09:14.280 --> 09:15.280] great.
[09:15.280 --> 09:18.800] So you see, it's going to be an event full of great talks, talking about technology,
[09:18.800 --> 09:23.280] of innovation, of applications, and it will also be presented by my dudev, who will surely
[09:23.280 --> 09:26.560] Many of you will know him, so you can't miss him.
[09:26.560 --> 09:30.320] I'll leave a link to the Samsung Dev website below in the description box
[09:30.320 --> 09:35.160] Spain, where you will find all the information regarding the agenda where you can register and a
[09:35.160 --> 09:37.040] a lot of other resources.
[09:37.040 --> 09:38.720] See you on 16 November.
[09:38.720 --> 09:43.400] Let's see how we can use Whisper in our own code.
[09:43.400 --> 09:47.240] For this we are going to use Google Colab, you know that Google is giving us here
[09:47.240 --> 09:52.080] a free virtual machine that we can use and we will check as long as we have
[09:52.080 --> 09:56.560] enabled the GPU hardware accelerated environment type, OK, let's hit it here
[09:56.560 --> 10:01.320] GPU, let's hit save and now the first step will be to install Whisper.
[10:01.320 --> 10:05.600] To do this we are going to use these two commands here, to install, you can find this here
[10:05.600 --> 10:11.160] in Whisper's own GitHub repository, I'm going to leave you below in the description box
[10:11.160 --> 10:14.160] these commands, hit run and let it install.
[10:14.160 --> 10:17.880] Once installed, we are going to upload some audio that we want to transcribe, in this case
[10:17.880 --> 10:21.920] I'm going to try Rosalía's song from Chicken Teriyaki, let's put it here,
[10:21.920 --> 10:26.800] we drag it and now the next step we are going to take it here and we are going to put the command
[10:26.800 --> 10:31.640] necessary to be able to run it, we're going to hit song.mp3 here, it's called the file that we
[10:31.640 --> 10:37.680] we have uploaded, okay, song.mp3, so the task is going to be to transcribe the size of the model,
[10:37.680 --> 10:42.560] there are different sizes depending on whether you want more speed when making the inference
[10:42.560 --> 10:46.920] or if you want more precision in the results, I usually work with the Medium model
[10:46.920 --> 10:50.600] which is the one that gives me good results, there are bigger models, there are smaller models, try it
[10:50.600 --> 10:55.360] and in this case simply where we are going to place the output file, we run
[10:55.360 --> 11:00.040] and that's it, that's it, no more to do, okay, we're already using Whisper,
[11:00.040 --> 11:03.660] the first time it will take a little while because you have to download the model but from this
[11:03.660 --> 11:08.520] At the moment you can use this system to transcribe any audio you want,
[11:08.520 --> 11:13.640] mola, ok, we can see that in this case it has detected that the language is Spanish, it has made the inference
[11:13.640 --> 11:16.800] automatic because we haven't told you that we are going to transcribe from Spanish, you can do it
[11:16.800 --> 11:20.960] if you want and when this cell is already executed, we can come here, we see
[11:20.960 --> 11:26.400] that the Audio Transcription folder has been generated and here we have the different options, we can
[11:26.400 --> 11:32.360] open the sound.txt and here we open the file, we can see that we have the whole song perfectly
[11:32.360 --> 11:37.000] transcribed, which in this case, being Rosalía, has more merit and instead of wanting to
[11:37.000 --> 11:41.680] transcription, you would like to make the translation, i.e. to convert your
[11:41.680 --> 11:45.640] voice, your audio to English, so all you have to do is change here the
[11:45.640 --> 11:51.480] task by Translate and in this case Whisper will work to translate what it has transcribed.
[11:51.480 --> 11:54.880] In this case, if you notice, the command we have used is the console command
[11:54.880 --> 11:58.480] but you may want to use Whisper within your code, then you can also
[11:58.480 --> 12:02.000] you have the option to work with Whisper's own library, it's simply this one
[12:02.000 --> 12:05.960] line of code from here, import it, load the model we want, here then
[12:05.960 --> 12:10.960] I would load the Medium model which is the one that, as I said, works best for my case, and with
[12:10.960 --> 12:17.520] the loaded model then here we call model.transcribe, let's put here song.mp3, we hit run
[12:17.520 --> 12:20.880] and in a matter of seconds we will have our transcript back.
[12:20.880 --> 12:24.520] And here it is, the Rosalia, pink without a card, I send it to your cat, I have it for you
[12:24.520 --> 12:27.600] with roulette, no need for a serenade, ok.
[12:27.600 --> 12:31.480] However, to make your life easier, I have prepared a notebook that you can use,
[12:31.480 --> 12:35.000] is below in the description box, where you already have all the code ready for
[12:35.000 --> 12:39.200] to start working, just log in, check that the GPU is activated,
[12:39.200 --> 12:43.080] click on this button here to install everything necessary, here we choose the
[12:43.080 --> 12:47.680] task we want to do, whether it is transcribing into any language or translating into English
[12:47.680 --> 12:48.800] and click on run.
[12:48.800 --> 12:53.520] In this case the cell is prepared so that the moment you start to run it
[12:53.520 --> 12:57.080] your microphone is recording right now, i.e. right now we would be generating
[12:57.080 --> 13:00.960] an audio file that we will then use for transcribing with Whisper, this is by
[13:00.960 --> 13:05.480] if you want to make a real-time transcript of any class or anything else
[13:05.480 --> 13:06.480] you need.
[13:06.480 --> 13:10.800] We're going to hit stop, we hit this button and in a moment we have the result of what we've done
[13:10.800 --> 13:12.520] we have said.
[13:12.520 --> 13:16.800] Below you will find the two commands needed to be able to transcribe or translate
[13:16.800 --> 13:19.240] the audio you upload.
[13:19.240 --> 13:22.760] Finally, you should also know that if you want something simpler, then there are pages
[13:22.760 --> 13:27.240] website where you can try out this system by uploading your own audios or by recording
[13:27.240 --> 13:28.240] from the microphone.
[13:28.240 --> 13:32.960] And this would be, 2022 is shaping up to be a spectacular year in terms of numbers
[13:32.960 --> 13:37.360] of neural toys that are coming into our hands to build a whole bunch
[13:37.360 --> 13:39.320] and to be able to touch them.
[13:39.320 --> 13:41.640] Now it's your turn, what can you do about it?
[13:41.640 --> 13:45.080] Well, you can build a lot of super interesting things, you can connect by
[13:45.080 --> 13:49.960] example Whisper with Stable Diffusion so that you can loudly ask it to
[13:49.960 --> 13:54.040] generate a table or you can for example take all your classes at the university or
[13:54.040 --> 13:58.960] all working meetings, transcribing them, creating a huge bank of transcripts and
[13:58.960 --> 14:03.680] then with the GPT-3 API to make a chatbot that allows you to query, ask questions
[14:03.680 --> 14:06.160] and answers on all these sources of information.
[14:06.160 --> 14:10.040] For example, something I want to do is to take all the videos from my YouTube channel
[14:10.040 --> 14:14.640] and transcribe it, generate good quality subtitles in both Spanish and English
[14:14.640 --> 14:18.920] and to be able to make statistics and queries on how many times I have said for example the word
[14:18.920 --> 14:19.920] Machine Learning.
[14:19.920 --> 14:23.360] There are a lot of applications that you can start to build, that you can start to build, that you can start to
[14:23.360 --> 14:27.160] create by combining all these technologies.
[14:27.160 --> 14:29.880] I had a dog barking in the background that was bothering me a lot.
[14:29.880 --> 14:34.080] Well, as I was saying, you can create a lot of things and there is a lot to do.
[14:34.080 --> 14:37.560] From here, from this channel, we will continue to experiment with this technology,
[14:37.560 --> 14:42.320] I will continue to bring you new tools so if you haven't done so yet, please subscribe,
[14:42.320 --> 14:46.000] click on the little bell to always receive notifications of new videos
[14:46.000 --> 14:50.440] and if you want to support all this content you know you can do so through Patreon
[14:50.440 --> 14:52.080] below in the description box.
[14:52.080 --> 14:55.080] You have a couple of videos around here that are super interesting, I don't know what they are but
[14:55.080 --> 14:58.960] are super interesting, keep an eye on them and we'll see you with more artificial intelligence
[14:58.960 --> 15:26.280] guys, girls, in the next video.
```

[audio_transcription/Whisper-Example_English (British)~alternative.txt](<audio_transcription/Whisper-Example_English%20(British)~alternative.txt>)

[audio_transcription/Whisper-Example_English (British)~alternative.vtt](<audio_transcription/Whisper-Example_English%20(British)~alternative.vtt>)

[audio_transcription/Whisper-Example_English (British)~alternative.srt](<audio_transcription/Whisper-Example_English%20(British)~alternative.srt>)

As a comparison, because in this case the target language is English, it can also be translated using Whisper directly.

**task**: `Translate to English`

```
[00:00.000 --> 00:06.400]  2022 will be remembered as the year of stable diffusion, of Dali 2, of incredible text
[00:06.400 --> 00:11.840]  generators models like Palm or code generators like AlphaCode. And yet, talking last month
[00:11.840 --> 00:16.880]  with Andres Torrubia, he told me that the most interesting thing he had seen this year was an
[00:16.880 --> 00:22.400]  artificial intelligence that came from the OpenAI laboratory, an AI called Whisper.
[00:22.400 --> 00:26.560]  What is the most impressive thing that has come out this year for you?
[00:26.560 --> 00:32.560]  Well, curiously, until now, Whisper, I think. Do you know why?
[00:32.560 --> 00:33.280]  Curious, huh?
[00:33.280 --> 00:39.840]  What impresses me about Whisper is that Whisper works, it's like, for me, Whisper, if it were the
[00:39.840 --> 00:47.680]  autonomous car, would be the first self-driving of the dictatorship. It is the first that looks like a person.
[00:47.680 --> 00:53.040]  Well, but for you to understand first what this Whisper is, I'm going to ask you to do the following exercise.
[00:53.040 --> 00:59.520]  I'm going to play an audio in English and your task is to transcribe each of the words you're listening to.
[00:59.520 --> 01:02.320]  Are you ready? 3, 2, 1.
[01:19.680 --> 01:21.200]  Have you understood anything?
[01:21.200 --> 01:22.560]  Yeah, me neither.
[01:22.560 --> 01:28.080]  Well, hearing this artificial intelligence, this is the perfect transcription you've got.
[01:28.080 --> 01:29.280]  And how about your Korean?
[01:29.280 --> 01:35.520]  Well, for Whisper it's not a problem either and you can also transcribe this audio in perfect English.
[01:44.320 --> 01:45.760]  And well, you understand me too.
[01:45.760 --> 01:52.480]  What you are seeing on the screen now is the speech to text that Whisper gets when he passes the audio track you are listening to.
[01:52.480 --> 02:00.080]  Look closely, not only does it get an almost perfect transcription, even understanding concrete words like Whisper or speech to text,
[02:00.080 --> 02:08.320]  but it is also able to generate points, commas and other punctuation marks that many other speech recognition commercial models are usually fed.
[02:08.320 --> 02:10.640]  And this is very interesting.
[02:10.640 --> 02:12.560]  Well, not this, but Whisper.
[02:12.560 --> 02:15.680]  Whisper in general has many interesting things.
[02:15.680 --> 02:19.840]  And the first interesting thing is the context in which this tool appears.
[02:19.840 --> 02:24.800]  After a year of incredible achievements by the OpenAI artificial intelligence laboratory,
[02:24.800 --> 02:32.800]  suddenly a collaborative initiative like Stability.ai emerges, which in September takes the lead in making Open Source
[02:32.800 --> 02:40.800]  many of the technologies that OpenAI, for its part, has decided to keep to itself and share only under paid services.
[02:40.800 --> 02:47.440]  For me this is not a problem either, since in the end OpenAI as a company has to pay its bills
[02:47.440 --> 02:52.080]  and at least it is giving us a way to access these powerful artificial intelligences.
[02:52.080 --> 02:53.520]  Learn Google.
[02:53.520 --> 03:01.840]  But of course, a new boy arrives in the city and begins to give candy to the children and suddenly the popular boy begins to look displaced.
[03:01.840 --> 03:06.880]  And at that precise moment, OpenAI arrives out of nowhere and gives us Whisper.
[03:06.880 --> 03:08.320]  For everyone's benefit.
[03:08.320 --> 03:11.280]  Because yes, friends, this is Open Source.
[03:11.280 --> 03:13.280]  I know you love to hear these words.
[03:13.280 --> 03:17.680]  At the end of the video I will show you a mini tutorial so you can see how easy it is to use this tool
[03:17.680 --> 03:21.440]  and I will also share a notebook so that it is super simple for you.
[03:21.440 --> 03:24.320]  And this is what makes Whisper a super interesting tool.
[03:24.320 --> 03:25.680]  But it's not the only thing.
[03:25.680 --> 03:28.720]  And this is where one of the things that has caught my attention the most comes from.
[03:28.720 --> 03:34.960]  And it is that Whisper is not a complex system that they have designed to process audio as it had never been done before,
[03:34.960 --> 03:38.720]  or a super complex system with a lot of processing modules.
[03:38.720 --> 03:39.360]  No.
[03:39.360 --> 03:45.520]  Whisper is this here, a transformer-type neural network from 2017.
[03:45.520 --> 03:47.520]  It has no change, no novelty.
[03:47.520 --> 03:51.040]  It is an architecture that we all know.
[03:51.040 --> 03:55.440]  So if this is so, why didn't a technology like Whisper already exist?
[03:55.440 --> 04:02.640]  Well, the key to making Whisper something so powerful is in the data and how they have structured their training.
[04:02.640 --> 04:10.640]  To train it, OpenAI has used no more or less than 680,000 hours of audio with its corresponding text.
[04:10.640 --> 04:12.240]  A brutality.
[04:12.240 --> 04:19.760]  And if you do the calculation, 680,000 hours, if you started playing them now, you would end up listening to it in 77 years.
[04:19.760 --> 04:23.920]  You could be sure that at some point in time you would see the comet Halley.
[04:23.920 --> 04:28.240]  But it is also a very interesting thing, is that these audios come in multiple languages,
[04:28.240 --> 04:35.280]  allowing us to train a model that is multilingual, that can understand us if we speak it in Spanish, English, Korean...
[04:35.280 --> 04:36.320]  It doesn't matter.
[04:36.320 --> 04:38.320]  But the thing is not just there.
[04:38.320 --> 04:43.440]  And it is that Whisper, in addition to being a multilingual system, is also a multitasking system.
[04:43.440 --> 04:49.600]  This is a trend that, as we saw in the video about Gato, is increasingly frequent in the world of deep learning.
[04:49.600 --> 04:55.520]  Not train AI for a single task, but train it for several different ones.
[04:55.520 --> 04:59.360]  Thus making its learning much more solid and robust.
[04:59.360 --> 05:03.920]  As we have seen, Whisper can take English audios and transcribe them to English.
[05:03.920 --> 05:06.560]  Or Korean audios and transcribe them to Korean.
[05:06.560 --> 05:10.560]  But the same model can also identify which language is being spoken.
[05:10.560 --> 05:16.320]  Or act as a voice detector to classify when a piece of audio is being heard, not a person.
[05:16.320 --> 05:19.760]  Or also the most interesting task, I think, of all.
[05:19.760 --> 05:25.520]  That you can speak to Whisper in any language and that he automatically transcribes it to English.
[05:25.520 --> 05:30.640]  And in this case I would not know why, but for me this seems to me a fascinating functionality.
[05:30.640 --> 05:32.800]  It seems that it does not offer us anything new, right?
[05:32.800 --> 05:39.200]  In the end you can take the text that any text transcriber generates in your language and pass it through a translator.
[05:39.200 --> 05:44.480]  But in this case it seems fascinating to me to see how something as simple as a single deep learning model
[05:44.480 --> 05:51.200]  allows you to speak in any language and that it generates the text in English without having to combine any type of tools.
[05:51.200 --> 05:53.200]  It's super simple.
[05:53.200 --> 05:56.160]  And the data we have commented on before is also super interesting.
[05:56.160 --> 06:03.120]  Because my first intuition here is that OpenAI, in the search for a massive data set of these 680,000 hours of audio
[06:03.120 --> 06:06.960]  that had a text transcription to be able to do this supervised learning,
[06:06.960 --> 06:12.400]  possibly had gone to one of the largest sources we can find on the internet, which is YouTube.
[06:12.400 --> 06:16.960]  In the end, you already know that all YouTube videos have automatically generated subtitles.
[06:16.960 --> 06:17.760]  Well, no.
[06:17.760 --> 06:24.080]  In this OpenAI emphasizes a lot in its paper to explain to us that they have made a filtering process
[06:24.080 --> 06:30.880]  to remove any text from the data set generated by automatic speech recognition systems.
[06:30.880 --> 06:31.520]  Why?
[06:31.520 --> 06:39.840]  Well, precisely to prevent Whisper from learning those defects, those vices that other automatic systems could also have.
[06:39.840 --> 06:43.360]  That said, now that we are talking about Whisper and YouTube,
[06:43.360 --> 06:48.000]  there is a theory that I want to tell you that I find very interesting, it is nothing that is confirmed,
[06:48.000 --> 06:55.440]  but that could explain the reason for the existence of this tool and that could have a certain relationship with a future GPT-4.
[06:55.440 --> 07:00.640]  This is an idea that I heard on the channel of Dr. Alan Thompson and that says that in the near future,
[07:00.640 --> 07:07.040]  where GPT-4 can start training, Whisper could offer the system a huge source of data
[07:07.040 --> 07:09.840]  that previous systems had not counted on.
[07:09.840 --> 07:14.560]  Let's think that a system like GPT-3 has been trained with a lot of Wikipedia articles,
[07:14.560 --> 07:17.440]  books, forums, internet conversations,
[07:17.440 --> 07:23.440]  but it has never been able to access all that spoken source that can be on databases such as YouTube.
[07:23.440 --> 07:27.600]  A tool like Whisper could be used to completely erase YouTube,
[07:27.600 --> 07:32.400]  transcribe many of its audios and unlock a new source of data
[07:32.400 --> 07:37.040]  that would not have been possible to use before to train a future language model.
[07:37.040 --> 07:39.760]  This is the enormous value that a tool like Whisper has,
[07:39.760 --> 07:42.560]  and that I think makes this technology so interesting.
[07:42.560 --> 07:47.520]  No, it does not solve a task that is spectacular, such as generating images or generating videos,
[07:47.520 --> 07:52.400]  but it solves a very useful task and almost solves it to perfection.
[07:52.400 --> 07:56.720]  Be careful, I say almost, it is not perfect, sometimes some words are obviously wrong
[07:56.720 --> 08:00.640]  and it does not cover all the languages ​​that exist on planet Earth,
[08:00.640 --> 08:03.840]  and well, for looking for some limitation compared to other commercial tools,
[08:03.840 --> 08:06.080]  it does not work in real time either.
[08:06.080 --> 08:08.960]  Still, processing audio, depending on the length,
[08:08.960 --> 08:12.240]  can take a few seconds, sometimes a minute,
[08:12.240 --> 08:15.040]  but it is a solid tool, it is mature, it is useful.
[08:15.040 --> 08:18.400]  And also open source, allowing anyone now
[08:18.400 --> 08:22.400]  can access a professional transcription and translation tool
[08:22.400 --> 08:25.520]  better than any free alternative.
[08:25.520 --> 08:28.480]  What? Oh, you also want to access this tool?
[08:28.480 --> 08:32.480]  Well, come on, I'll prepare an easy tutorial for you so you can all use it,
[08:32.480 --> 08:34.000]  we will do it in Google Colab.
[08:34.000 --> 08:37.520]  But before, and taking advantage of the fact that we are talking about programming,
[08:37.520 --> 08:41.920]  development, innovation, let me remind you that there are very few days left
[08:41.920 --> 08:44.800]  for the Samsung Dev Day to be celebrated,
[08:44.800 --> 08:49.280]  which is the technological event that the Samsung Dev Spain community celebrates every year,
[08:49.280 --> 08:52.800]  which is the official Samsung community for Spanish developers.
[08:52.800 --> 08:55.520]  This will be a free event that you cannot miss.
[08:55.520 --> 08:59.760]  If you are in Madrid, you can attend in person on November 16
[08:59.760 --> 09:02.480]  at the Clostro de los Jerónimos of the Museo del Prado.
[09:02.480 --> 09:05.520]  And if not, you can connect online through its streaming.
[09:05.520 --> 09:07.440]  But yes, you have to register.
[09:07.440 --> 09:09.520]  I was lucky last year to be able to participate
[09:09.520 --> 09:13.120]  with a paper on the generation of code with artificial intelligence
[09:13.120 --> 09:14.800]  and the experience was great.
[09:14.800 --> 09:17.520]  So you see, it will be an event full of great talks,
[09:17.520 --> 09:20.480]  talking about technology, innovation, applications,
[09:20.480 --> 09:22.720]  and it will also be presented by my Dudef,
[09:22.720 --> 09:25.280]  which surely many of you know him,
[09:25.280 --> 09:26.560]  so you can't miss it.
[09:26.560 --> 09:28.800]  I'll leave you a link in the description box
[09:28.800 --> 09:30.720]  to the Samsung Dev Spain website,
[09:30.720 --> 09:33.600]  where you will find all the information regarding the agenda,
[09:33.600 --> 09:36.880]  where to register and a lot of other resources.
[09:36.880 --> 09:38.800]  See you on November 16.
[09:38.800 --> 09:43.200]  Well, let's see how we can use Whisper in our own code.
[09:43.200 --> 09:45.360]  For this, we are going to use Google Call App.
[09:45.360 --> 09:48.800]  You already know that Google is giving us a free virtual machine
[09:48.800 --> 09:50.880]  that we can use and we are going to verify
[09:50.880 --> 09:53.520]  whenever we have activated the type of environment
[09:53.520 --> 09:55.520]  with hardware acceleration GPU.
[09:55.520 --> 09:56.800]  Okay, let's give it here.
[09:56.800 --> 09:58.240]  GPU, let's save it.
[09:58.240 --> 10:01.040]  And now the first step will be to install Whisper.
[10:01.040 --> 10:04.160]  For this, we are going to use these two commands here.
[10:04.160 --> 10:08.560]  Install, you can find this in the GitHub Whisper repository itself.
[10:08.560 --> 10:10.800]  I'll leave you down in the description box.
[10:10.800 --> 10:14.000]  These commands, we give it to run and let it install.
[10:14.000 --> 10:16.160]  Once installed, we are going to upload some audio
[10:16.160 --> 10:17.200]  that we want to transcribe.
[10:17.200 --> 10:19.600]  In this case, I'm going to try with the song of Rosalia
[10:19.600 --> 10:20.640]  by Chicken Teriyaki.
[10:20.640 --> 10:22.560]  Let's put it here, we drag it.
[10:22.560 --> 10:25.040]  And now the next step, we're going to take it here
[10:25.040 --> 10:28.320]  and we're going to put the command we need to run it.
[10:28.320 --> 10:30.720]  We're going to give it here to song.mp3.
[10:30.720 --> 10:32.560]  It's called the file we've uploaded.
[10:32.560 --> 10:34.640]  Okay, song.mp3.
[10:34.640 --> 10:37.520]  The task is going to be to transcribe the size of the model.
[10:37.520 --> 10:38.560]  There are different sizes,
[10:38.560 --> 10:42.400]  depending on whether you want more speed when doing the inference
[10:42.400 --> 10:44.960]  or if you want more precision in the results.
[10:44.960 --> 10:46.800]  I usually work with the medium model,
[10:46.800 --> 10:48.320]  which is the one that gives me good results.
[10:48.320 --> 10:50.000]  There are larger models, there are smaller models.
[10:50.000 --> 10:50.480]  Try it.
[10:50.480 --> 10:54.320]  And in this case, we're just going to put the output file.
[10:54.320 --> 10:56.000]  We run it and that's it.
[10:56.000 --> 10:56.480]  That's it.
[10:56.480 --> 10:57.840]  There's nothing else to do.
[10:57.840 --> 10:59.840]  Okay, we're using Whisper.
[10:59.840 --> 11:01.520]  The first time it will take a while
[11:01.520 --> 11:02.800]  because it has to download the model,
[11:02.800 --> 11:04.080]  but from this moment on,
[11:04.080 --> 11:06.480]  you can use this system to transcribe
[11:06.480 --> 11:08.560]  any audio you want.
[11:08.560 --> 11:09.200]  Cool.
[11:09.200 --> 11:11.040]  Okay, we see that in this case it has detected
[11:11.040 --> 11:12.400]  that the language is Spanish.
[11:12.400 --> 11:14.080]  It has made the automatic inference
[11:14.080 --> 11:16.160]  because we have not told it that we are going to transcribe in Spanish.
[11:16.160 --> 11:17.440]  You can do it if you want.
[11:17.440 --> 11:19.040]  And when this cell is already executed,
[11:19.040 --> 11:20.480]  we can come over here.
[11:20.480 --> 11:23.040]  We see that the audio transcription folder has been generated
[11:23.040 --> 11:25.840]  and here we have the different options.
[11:25.840 --> 11:28.000]  We can open the sound.txt
[11:28.000 --> 11:29.120]  and here we open the file.
[11:29.120 --> 11:32.800]  We see that we have the whole song perfectly transcribed,
[11:32.800 --> 11:35.600]  which in this case, being Rosalía, has more merit.
[11:35.600 --> 11:38.000]  If instead of wanting to do the transcription,
[11:38.000 --> 11:40.000]  you would like to do the translation,
[11:40.000 --> 11:43.840]  that is, convert your voice, your audio to English,
[11:43.840 --> 11:46.800]  then all you have to do is change the task here for translate.
[11:46.800 --> 11:49.840]  And in this case, Whisper will work to translate
[11:49.840 --> 11:51.360]  what it has transcribed.
[11:51.360 --> 11:52.480]  In this case, if you notice,
[11:52.480 --> 11:54.880]  the command we have used has been the console one,
[11:54.880 --> 11:57.920]  but maybe you want to use Whisper within your code.
[11:57.920 --> 11:59.440]  Then you also have the option of working
[11:59.440 --> 12:01.040]  with the Whisper library itself.
[12:01.040 --> 12:03.120]  It's just this line of code here.
[12:03.120 --> 12:05.360]  We import it, we load the model we want.
[12:05.360 --> 12:07.520]  Here, I would load the medium model,
[12:07.520 --> 12:10.480]  which is the one that, as I say, works best for my case.
[12:10.480 --> 12:11.600]  And with the loaded model,
[12:11.600 --> 12:14.160]  then here we call model.transcribe.
[12:14.160 --> 12:16.400]  We are going to put here song.mp3.
[12:16.400 --> 12:18.560]  We hit run and in a matter of seconds,
[12:18.560 --> 12:20.720]  we will have our transcription again.
[12:20.720 --> 12:21.440]  And here we have it.
[12:21.440 --> 12:23.920]  The pink rose without a card, I send it to your cat,
[12:23.920 --> 12:26.080]  I have it with a roulette, no need to serenade.
[12:26.080 --> 12:26.580]  Well, shock.
[12:27.120 --> 12:28.800]  Also to make your life easier,
[12:28.800 --> 12:31.120]  I have prepared a notebook that you can use.
[12:31.120 --> 12:32.960]  It's down in the description box,
[12:32.960 --> 12:35.920]  where you already have all the code ready to start working.
[12:35.920 --> 12:37.040]  You just have to enter,
[12:37.040 --> 12:38.960]  check that the GPU is activated,
[12:38.960 --> 12:42.160]  we hit this button here to install everything necessary.
[12:42.160 --> 12:44.000]  Here we choose the task we want to do,
[12:44.000 --> 12:47.520]  because if it is to transcribe to any language or translate to English,
[12:47.520 --> 12:48.640]  and we hit run.
[12:48.640 --> 12:50.240]  In this case, the cell is prepared
[12:50.240 --> 12:53.440]  so that the moment you start to run it,
[12:53.440 --> 12:55.120]  it is recording your microphone right now.
[12:55.120 --> 12:57.920]  That is, right now we would be generating an audio file
[12:57.920 --> 13:00.400]  that we will later use to transcribe with Whisper.
[13:00.400 --> 13:03.520]  This is in case you want to make a transcription in real time
[13:03.520 --> 13:06.160]  of any class or anything you need.
[13:06.160 --> 13:07.920]  We're going to stop it, we hit this button,
[13:08.560 --> 13:12.000]  and in a moment we have the result of what we have said.
[13:12.000 --> 13:14.800]  Likewise, then below I add the two commands necessary
[13:14.800 --> 13:18.960]  to be able to transcribe or translate the audio that you upload.
[13:18.960 --> 13:21.840]  Finally, you also have to know that if you want something simpler,
[13:21.840 --> 13:24.960]  there is a website where you can try this system
[13:24.960 --> 13:28.160]  by uploading your own audios or recording from the microphone.
[13:28.160 --> 13:28.880]  And this would be.
[13:28.880 --> 13:31.920]  2022 is really looking like a spectacular year
[13:31.920 --> 13:34.240]  in terms of the number of neural toys
[13:34.240 --> 13:35.440]  that are coming to our hands
[13:35.440 --> 13:39.200]  to build a lot of tools and to be able to touch them.
[13:39.200 --> 13:40.160]  Now it's your turn.
[13:40.160 --> 13:41.360]  What can you do with this?
[13:41.360 --> 13:44.240]  Well, you can build a lot of super interesting things.
[13:44.240 --> 13:47.040]  You can connect, for example, Whisper with Stable Diffusion
[13:47.040 --> 13:50.720]  so that you can ask it to generate a picture.
[13:50.720 --> 13:53.840]  Or you can, for example, take all your classes at the university
[13:53.840 --> 13:56.640]  or all the work meetings, transcribe them,
[13:56.640 --> 13:58.720]  create a huge bank of transcriptions
[13:58.720 --> 14:01.600]  and then with the GPT-3 API make a chatbot
[14:01.600 --> 14:04.160]  that allows you to consult, ask questions and answers
[14:04.160 --> 14:05.920]  about all that source of information.
[14:05.920 --> 14:07.360]  For example, something I want to do
[14:07.360 --> 14:09.920]  is take all the videos from my YouTube channel
[14:09.920 --> 14:12.880]  and transcribe them, generate good quality subtitles
[14:12.880 --> 14:14.480]  both in Spanish and in English
[14:14.480 --> 14:16.560]  and be able to do statistics and consultations
[14:16.560 --> 14:19.760]  of how many times I have said, for example, the word machine learning.
[14:19.760 --> 14:22.560]  There are a lot of applications that you can start building,
[14:22.560 --> 14:26.800]  that you can start creating by combining all these technologies.
[14:26.800 --> 14:28.080]  There is also a barking dog in the background
[14:28.080 --> 14:29.520]  that was bothering me a lot.
[14:29.520 --> 14:30.800]  Well, what I was saying,
[14:30.800 --> 14:33.920]  that you can create a lot of things and there is a lot to do.
[14:33.920 --> 14:36.400]  From here, from this channel, we will continue to do experiments
[14:36.400 --> 14:37.360]  with this technology.
[14:37.360 --> 14:39.600]  I will continue to bring new tools
[14:39.600 --> 14:42.000]  so if you haven't done it yet, subscribe,
[14:42.000 --> 14:44.720]  hit the bell so you always get notifications
[14:44.720 --> 14:45.840]  that there is a new video
[14:45.840 --> 14:47.600]  and if you want to support all this content,
[14:47.600 --> 14:50.320]  you already know that you can do it through Patreon
[14:50.320 --> 14:51.840]  below in the description box.
[14:51.840 --> 14:54.000]  You have a couple of videos around here that are super interesting,
[14:54.000 --> 14:55.840]  I don't know which ones they are, but they are super interesting,
[14:55.840 --> 14:56.880]  take a look at them
[14:56.880 --> 14:58.880]  and see you with more artificial intelligence,
[14:58.880 --> 15:10.880]  guys, girls, in the next video.
```

[audio_transcription/Whisper-Example_English.txt](audio_transcription/Whisper-Example_English.txt)

[audio_transcription/Whisper-Example_English.vtt](audio_transcription/Whisper-Example_English.vtt)

[audio_transcription/Whisper-Example_English.srt](audio_transcription/Whisper-Example_English.srt)
