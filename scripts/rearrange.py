import sys
import random

def scramble():
    args = sys.argv[1:]
    newList = []
    for _ in range(len(args)):
        rand = random.randint(0, len(args)-1)
        if args[rand] not in newList:
            newList.append(args[rand])
    return ' '.join(newList)

print("""
    < {} >
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """.format(scramble()))
