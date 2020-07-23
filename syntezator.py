from gtts import gTTS
from playsound import playsound
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = 'Witaj przybyszu!'
  
# Language in which you want to convert 
language = 'pl'

myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 

playsound("welcome.mp3")