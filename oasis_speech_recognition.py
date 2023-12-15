import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speechi
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def greet():
    engine.say("Hello! How can I help you? please tell me")
    engine.runAndWait()

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    engine.say(f"The current time is {current_time}")
    engine.runAndWait()

def tell_date():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    engine.say(f"Today is {current_date}")
    engine.runAndWait()

def web_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        engine.say("Sorry, I didn't understand that.")
        engine.runAndWait()
        return ""
    except sr.RequestError:
        print("Sorry, I'm unable to process your request at the moment.")
        return ""

if __name__ == "__main__":
    greet()
    while True:
        command = listen()
        
        if "hello" in command:
            greet()
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                web_search(query)
            else:
                engine.say("What do you want to search for?")
                engine.runAndWait()
        elif "exit" in command or "bye" in command:
            engine.say("Goodbye! thanks for using me")
            engine.runAndWait()
            break
