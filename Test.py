#from gtts import gTTS
import time
from pygame import mixer # Load the required library
#tts = gTTS(text="Welcome to the Marathon.  I am Leela, one of the two surviving Artificial Intelligences aboard the Marathon.  I have been severely damaged, and am working to understand the current situation. Find the teleport terminal located in the Hangar's control room.  By that time, I should have a better idea of what is going on.", lang='en')
#tts.save("good.mp3")
mixer.init()
mixer.music.load('good.mp3')
mixer.music.play()
time.sleep(30)
mixer.music.load('Heart_of_Machine.mp3')
mixer.music.play()
mixer.music.fadeout(5600)