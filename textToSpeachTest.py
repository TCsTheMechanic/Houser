import os
import speech_recognition as sr
houser = sr.Recognizer()

speech = ""

while(speech != "goodbye Houser"):
    with sr.Microphone() as source:
        print("----------Start----------")
        audio = houser.listen(source)
        print("----recording is over----")

    try:
        speech = "" + houser.recognize_google(audio)
        print("Person said: " + speech)
        if(speech == "hello Houser"):
            os.system("cd audios & hello.mp3")
        elif(speech == "good night") or (speech == "good night Houser"):
            os.system("cd audios & goodNight.mp3")
        elif(speech == "goodbye Houser"):
            os.system("cd audios & bye.mp3")
        elif (speech == "how are you"):
            os.system("cd audios & fineThink.mp3")
        else:
            os.system("cd audios & repeatPlz.mp3")
    except:
        pass
