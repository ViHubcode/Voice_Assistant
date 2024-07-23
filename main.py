import speech_recognition as sr
from pyttsx3 import init as pyttsx3_init
import datetime
from modules import weather
from modules import open_
from modules.YT_auto import music
from modules.selenium_web_driver import inforr
from modules.News import news
from modules.search import sear
import random
import math


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 16:
        return "Afternoon"
    elif 16 <= hour < 19:
        return "Evening"
    else:
        return "Night"


engine = pyttsx3_init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

API_KEY = '180daa00b22bb685a35bdb644c682968'  # Your OpenWeatherMap API key

# Initialize the recognizer
recognizer = sr.Recognizer()

while True:
    speak("What can I do for you?")

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        # Example usage of weather module
        if "temperature" in text:
            speak("Sure,Which city's weather would you like to know?")
            CITY= input("Which city's weather would you like to know? ")
            weather_info = weather.get_weather(API_KEY, CITY)
            if weather_info:
                temperature = weather_info["temperature"]
                description = weather_info["description"]
                print(f"Temperature in {CITY} is {temperature}°C with {description}.")
                speak(f"Temperature in {CITY} is {temperature} degrees Celsius with {description}.")
            else:
                print("Unable to fetch weather information.")
                speak("Unable to fetch weather information.")

        # Example usage of open module
        elif "open file" in text:
            speak("Sure, sir. Please provide the file path.")
            file_path = input("Please provide the file path: ")
            open_.open_file(file_path)

        # Example usage of music module
        elif "play video" in text:
            speak("Sure, sir. Which video do you want me to play?")
            vid = input("Which video do you want me to play? ")
            speak(f"Playing {vid} on YouTube")
            assistant = music()
            assistant.play(vid)

        # Example usage of inforr module
        elif "information" in text:
            speak("You need information related to which topic")
            infor = input("You need information related to which topic? ")
            speak(f"Searching {infor} in Wikipedia")
            assist = inforr()
            assist.get_info(infor)

        # Example usage of news module
        elif "news" in text:
            speak("Sure sir, now I will read news for you")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

        # Example usage of sear module
        elif "search" in text:
            speak("What should I search for, sir?")
            searc = input("What should I search for? ")
            speak(f"Searching {searc} in Google")
            assist = sear()
            assist.get_infoo(searc)

        # Example usage of guessing game
        elif "game" in text:
            speak("Enter your lower limit, sir")
            lower = int(input("Enter your lower limit: "))
            speak("Now, enter your upper limit")
            upper = int(input("Enter your upper limit: "))
            x = random.randint(lower, upper)
            speak(f"\nYou've only {round(math.log(upper - lower + 1, 2))} chances to guess the integer!\n")
            print(f"\nYou've only {round(math.log(upper - lower + 1, 2))} chances to guess the integer!\n")
            print(f"Number is between {lower} and {upper}")

            count = 0
            while count < math.log(upper - lower + 1, 2):
                count += 1
                speak("Start guessing")
                speak("Guess a number")
                guess = int(input("Guess a number: "))
                if x == guess:
                    print(f"Congratulations, you did it in {count} tries")
                    speak(f"Congratulations, you did it in {count} tries")
                    break
                elif x > guess:
                    print("You guessed too small!")
                    speak("You guessed too small!")
                elif x < guess:
                    print("You guessed too high!")
                    speak("You guessed too high!")

            if count >= math.log(upper - lower + 1, 2):
                print(f"\nThe number was {x}")
                speak(f"\nThe number was {x}")
                print("\tBetter Luck Next time!")
                speak("\tBetter Luck Next time!")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
