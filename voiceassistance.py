import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Set pause threshold to 1 second
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f"You said: {query}")
            return query.lower()

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

# Main loop
while True:
    command = listen()

    if command.startswith("hello"):
        speak("Hello! How can I assist you?")
    elif command.startswith("goodbye"):
        speak("Goodbye!")
        break
    elif command == "":
        continue
    else:
        speak("I'm sorry, I cannot perform that command.")
