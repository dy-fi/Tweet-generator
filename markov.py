import dictogram
from collections import Counter
import frequency_analysis
import sys

def dictogram(words):
    hist = Dictogram(words)
    for i in range(len(words) - 1):
        hist[words[i]].add_count(hist[words[i+1]])
    return hist


if __name__ == "__main__":
    words = sys.argv[1]
    print(dictogram(words))
