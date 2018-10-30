from collections import Counter
import sys

def histogram(words):
    """
        Takes an argument(corpus) and returns the times each word is used
    """
    count = Counter()
    for word in words:
        count[word] += 1
    return count

if __name__ == '__main__':
    words = open(sys.argv[1], "r").read().split()
    print(histogram(words))
