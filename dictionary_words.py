import sys
import random

words = open("/usr/share/dict/words", "r").read().split('\n')
numWords = sys.argv[1]
newSentence = []

for i in range(int(numWords)):
    newSentence.append(words[random.randint(0, len(words))] + " ")

print(''.join(newSentence))
