import random

def getRandomWords(numWords):
    """
        Takes an argument(int) and returns that many random words
    """
    words = open("/usr/share/dict/words", "r").read().split('\n')
    newSentence = []
    for i in range(int(numWords)):
        newSentence.append(words[random.randint(0, len(words))] + " ")
    return(''.join(newSentence))

if __name__ == "__main__":
    import sys
    numWords = sys.argv[1]
    print(getRandomWords(numWords))
