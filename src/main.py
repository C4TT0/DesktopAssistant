from Utility.speak import Speak
from Utility.listen import listen

# Configuring Voice

Speak.change_rate(120)
Speak.change_voice(1)


if __name__ == '__main__':
    Speak.speak(listen())
