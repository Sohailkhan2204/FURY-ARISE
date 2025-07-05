import speech_recognition as sr
import pyttsx3
import musiclibrary
import webbrowser

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Function to speak the given text."""
    tts_engine.say(text)
    tts_engine.runAndWait()
def processcommand(c):
    print("Processing command:", c)
    """Function to process the recognized command."""
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")
    elif c.lower().startswith("play "):
        song=c.lower().split(" ")[1]# play perfect -> space split -> ['play', 'perfect'] ->index 1 -> 'perfect'
        link=musiclibrary.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}")
    
# Set properties for the TTS engine
tts_engine.setProperty('rate', 250)  # Speed of speech
tts_engine.setProperty('volume', 0.8)  # Volume level (0.0 to 1.0)
voices =tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)

if __name__ == "__main__":
    # Initialize the recognizer and the text-to-speech engine

    speak("call me when you need me")
    while True:
        # Use the microphone as the audio source

        try:
            with sr.Microphone() as source:
                print("listening...")
                
                audio = recognizer.listen(source,timeout=5, phrase_time_limit=3)
            # Recognize speech using Google Web Speech API
            wakeupcall= recognizer.recognize_google(audio)
            if(wakeupcall.lower() == "fury arise"):
                print("Wake word detected:")
                speak("i stand ready my lord")
                #listen for the next command
                with sr.Microphone() as source:
                    print("listening...")
                    audio = recognizer.listen(source)
                    inputvoice = recognizer.recognize_google(audio)

                    processcommand(inputvoice)

        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")

