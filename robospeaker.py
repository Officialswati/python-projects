from gtts import gTTS
import os
if __name__=='__main__':
    print("Welcome to robospeaker 1.1 created by Swati. :")
    while True:
        x = input("Enter what you want me to speak:")
        if(x=="q"):
            y="bye bye friend meet you soon :"
            language='en'
            myobj = gTTS(text = y, lang=language , slow= False)
            myobj.save("y.mp3")
            os.system("start y.mp3")
            break
        language = 'en'
        myobj = gTTS(text = x, lang=language , slow= False)
        myobj.save("welcome.mp3")
        os.system("start welcome.mp3")