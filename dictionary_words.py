import sys
import random

words = open("/usr/share/dict/words", "r").read().split('\n')
numWords = sys.argv[1]

def getRandomWords(words, numWords):
    newSentence = []
    for i in range(int(numWords)):
        newSentence.append(words[random.randint(0, len(words))] + " ")
    return(''.join(newSentence))

print(getRandomWords())
