# I absolutely couldn't find a way of how to run this Python script and return the result 
# back to my Node.js application. Tried every solution online but I'll have to find a solution later

import speech_recognition as sr
import sys

# Grabs audio through Google's Speech Recogonition API
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Begin speaking')
    audio = r.listen(source)

print('You said: ' + r.recognize_google(audio))
wordsArr = r.recognize_google(audio).split(" ") # Splits entire audio into list containing each separate word
print(wordsArr)

# TODO: Work on implementing a better algorithm to locate keywords given by user audio.
# Instead of comparing all words with a predefined keyword list

def search():
    keywords = ['food', 'shelter', 'drugs', 'church', 'hospital']
    for word in wordsArr:
        if word in keywords:
            return word
    return -1

result = search()
print(result)



