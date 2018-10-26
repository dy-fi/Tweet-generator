from nltk.corpus import wordnet
import sys
import random

def define(word):
    syns = nltk.synsets("game")
    print(syns[0].definition())


def getRandomWords(words, numWords):
    newSentence = []

    for i in range(int(numWords)):
        newSentence.append(words[random.randint(0, len(words))] + " ")

    return(''.join(newSentence))


def game():
    words = open("/usr/share/dict/words", "r").read().split('\n')
    word = getRandomWords(words, 1)
    _ = input("Guess the definition of the word and then it will be shown: " + word)
    define(word)
    uinput = input("Do you want to continue? (y/n)")
    if uinput.lower() == "n":
        return False
    else:
        return True

cont = True
while(cont):
    cont = game()
