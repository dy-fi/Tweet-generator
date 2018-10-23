import sys
import random

def scramble():
    args = sys.argv[1:]
    newList = []
    for i in range(len(args)+2):
        rand = random.randint(0, len(args)-1)
        if args[rand] not in newList:
            newList.append(args[rand])
    return newList

print(scramble())
