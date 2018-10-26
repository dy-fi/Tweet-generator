from collections import Counter
import sys

def histogram(words):
    count = Counter()
    for word in words:
        count[word] += 1
    return count

filename = sys.argv[1]
words = open(sys.argv[1], "r").read().split()
print(histogram(words))
