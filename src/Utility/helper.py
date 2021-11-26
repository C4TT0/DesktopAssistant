from Utility.speak import Speak
import datetime


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        Speak.speak("Good Morning !")
    elif 12 <= hour < 18:
        Speak.speak("Good Afternoon")
    else:
        speak("Good Evening !")
