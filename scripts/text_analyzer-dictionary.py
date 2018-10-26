import sys

def histogram():
    filename = sys.argv[1]
    words = open(sys.argv[1], "r").read().split()
    dict = {"word": 0}
    for word in words:
        dict[word] = 0
    for word in words:
        dict[word] += 1
    return dict

print(histogram())
