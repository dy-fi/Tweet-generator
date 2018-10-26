import sys

def histogram(words):
    dict = {"word": 0}
    for word in words:
        dict[word] = 0
    for word in words:
        dict[word] += 1
    return dict

filename = sys.argv[1]
words = open(sys.argv[1], "r").read().split()
print(histogram(words))
