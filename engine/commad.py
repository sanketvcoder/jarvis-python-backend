import pyttsx3
import speech_recognition as sr
import eel


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Female voice (Change to voices[0] for male)
    engine.setProperty('rate', 125)  # Adjust speech speed
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.displayMessage('Listening...')
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        
        try:
            audio = r.listen(source)  # ✅ Waits indefinitely until the user speaks
            print("Recognizing...")
            eel.displayMessage('Recognizing...')
            query = r.recognize_google(audio, language='en-in')  # Using Google Speech Recognition
            print(f"User said: {query}")
            eel.displayMessage(query)
            speak(query)
            eel.show()
            return query.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Speech Recognition service is unavailable.")
            return ""


