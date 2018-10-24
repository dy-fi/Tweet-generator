import sys
import random
from collections import Counter

f = open("/usr/share/dict/words", "r")
words = f.readlines()
numWords = sys.argv[1]
newSentence = []

for i in range(int(numWords)):
    newSentence += words[random.randint(0, len(words))]

print(''.join(newSentence))
f.close()
