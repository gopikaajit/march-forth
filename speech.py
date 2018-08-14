#!/usr/bin/python

#SPEECH RECOGNITION MODULE OF PYTHON
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass


#SPECCH TO WORDS SPLITTING




import cv2
import numpy as np 
listi=[]
dicti={'my':'my.png','name':'name.png','is':'is.jpeg','ann':'ann.jpeg','how':'how.jpeg','you':'you.jpeg','hello':'hello.jpeg','world':'world.jpeg','i':'i.png','am':'am.jpeg','happy':'happy.jpeg','goodmorning':'goodmorning.jpeg','goodafternoon':'goodafternoon.jpeg','love':'love.jpeg','ready':'ready.jpeg','be':'be.jpeg','strong':'strong.png','fine':'fine.jpeg','get':'get.jpeg','today':'today.jpeg','it':'it.jpeg','raining':'raining.jpeg'}

def getword(a):
#count=0
	for word in a.split():
		listi.append(word)
		#count=count+1
	for word in listi:
		print word
		for k in dicti:
			if(word==k):
				image=cv2.imread(dicti[k],0)
				img=cv2.resize(image,(2000,1000))
				cv2.imshow('image',img)
				cv2.waitKey(0)	
a=raw_input("enter string")
getword(a)



