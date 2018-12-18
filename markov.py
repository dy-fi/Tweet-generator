from dictogram import Dictogram
import frequency_analysis
import sys

def dictogram(words):
    hist = Dictogram()
    for i in range(len(words)-1):
        if words[i] not in hist:
            hist[words[i]] = Dictogram()
        hist[words[i]].add_count(words[i+1])


if __name__ == "__main__":
    words = sys.argv[1]
    print(dictogram(words))
