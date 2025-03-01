from playsound import playsound
import eel
#Playing Assistant sound function

@eel.expose
def playAssistanceSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


