import pyttsx3

engine = pyttsx3.init()


# Everything related to speaking functionality

class Speak:
    def __init__(self):
        pass

    @staticmethod
    def change_rate(rate_inp):
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate_inp)

    @staticmethod
    def change_voice(voice):
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice].id)

    @staticmethod
    def speak(txt: str):
        engine.say(txt)
        engine.runAndWait()
        engine.stop()
