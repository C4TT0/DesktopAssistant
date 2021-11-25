import speech_recognition as sr

r = sr.Recognizer()


def listen():
    while 1:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)

                text = r.recognize_google(audio2)
                text = text.lower()

                return text
        except sr.RequestError as e:
            return f"Could not request results: {e}"
        # except sr.UnknownValueError:
        #     return "Unknown error Occurred"
