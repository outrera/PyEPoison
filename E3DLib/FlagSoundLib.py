import pygame
import time
from pathlib import Path
import speech_recognition as sr
from gtts import gTTS

"""
Debido a que no se puede intercambiar directamente información desde entidad 3d a python, el siguiente
comando verificará constantemente la existencia de un archivo, mientras ese archivo exista se reproducirá
el sonido especificado.
Dummypath: Nombre del archivo que el comando comprobará su existencia (Con terminación)
file: Nombre del archivo que se reproducirá (Con terminación)
chan: Número de canal que se desea usar
fadetime: Tiempo (en segundos) que se tardará en desvanecerse el sonido
"""
def flag_sound(Dummypath,file,chan,fadetime):
	my_file = Path("/"+Dummypath)
	dummycond=0
	while dummycond==0
		try:
		my_abs_path = my_file.resolve():
		except FileNotFoundError:
			if enabled==True
				mixer.sound.fadeout(fadetime)
				enabled=False
			break
		else:
			if enabled==False:
				sound=pygame.mixer.Channel(chan)
				mixer.init()
				mixer.sound.load("/wav/"+file)
				mixer.sound.play()
				enabled=True
	time.sleep(5)
"""
Este comando es un ejemplo de cómo funcionaría un sistema de reconocimiento
de voz y cómo este podría ser transformado en audio o crear una respuesta según
condiciones.
Depende de una conexión a internet y de un microfono.
"""
def flag_sound_repeat()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        recon = r.recognize_google(audio)
        # recognize speech using Google Speech Recognition
        try:
            stamp=("Google Speech Recognition thinks you said " + recon)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))print(stamp)

		tts = gTTS(text=stamp, lang='en')
		tts.save("good.mp3")
		mixer.init()
		mixer.music.load('good.mp3')
		mixer.music.play()
