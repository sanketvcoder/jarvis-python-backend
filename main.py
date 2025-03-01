import os
import eel
from engine.features import * 


eel.init("www") # all front end files

playAssistanceSound()

os.system('start msedge.exe --app="http://127.0.0.1:5000/index.html"')

eel.start('index.html', mode = None, host ='localhost', port=5000, block  =True)
