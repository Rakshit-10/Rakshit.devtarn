import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Could not understand audio")
        command = None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        command = None

    return command


if __name__ == "__main__":
    speak("Hello! I am your Python assistant. How can I help you today?")

    while True:
        command = listen()

        if command is not None:
            if "hello" in command:
                speak("Hello there!")
            elif "how are you" in command:
                speak("I'm fine, thank you!")
            elif "goodbye" in command:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't understand that command.")
        else:
            speak("I'm sorry, I didn't catch that. Could you please repeat?")
