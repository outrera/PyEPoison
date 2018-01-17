import speech_recognition as sr
from gtts import gTTS
import time
from pygame import mixer # Load the required library
# obtain audio from the microphone


ak='what results from the chemical reaction of water and sodium'
if recon == ak:
	tts = gTTS(text="It results in caustic sose and hidrogen, oh, and also an explosion", lang='en')
	tts.save("sodium.mp3")
	mixer.init()
	mixer.music.load('sodium.mp3')
	mixer.music.play()
