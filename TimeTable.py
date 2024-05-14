import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180-200)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


FiveTo7 = '''
It's time to wake up,
and do some exercises
5 am to 7 am,
thanks.
'''
SevenTo12 = '''
It's time for your school classes,
Please be ready
7 am to 12 pm,
thanks.
'''
TwelveTo14 = '''
Its time for lunch and some rest,
12 pm to 2 pm,
thanks.
'''
FourteenTo17 = '''
It's time for study,
2 pm to 5:30 pm,
thanks.
'''
SeventeenTo20 = '''
Tuition time is ariving
you should rest and then
you should get ready
5:30 pm to 8 pm,
thanks.
'''
TwentyTo22 = '''
It's time for dinner
8 pm to 10 pm
thanks.
'''
def Time():
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour>=5 and hour<=7:
        speak(FiveTo7)
        return FiveTo7
    elif hour>=7 and hour<=12:
        speak(SevenTo12)
        return SevenTo12
    elif hour>=12 and hour<=14:
        speak(TwelveTo14)
        return TwelveTo14
    elif hour>=14 and hour<=17:
        speak(FourteenTo17)
        return FourteenTo17
    elif hour>=17 and hour<=20:
        speak(SeventeenTo20)
        return SeventeenTo20
    elif hour>=20 and hour<=22:
        speak(TwentyTo22)
        return TwentyTo22
    else:
        speak("In this time, you have to sleep")