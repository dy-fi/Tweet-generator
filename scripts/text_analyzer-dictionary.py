import sys

def histogram(words):
    """
        Takes an argument(corpus) and returns the times each word is used
    """

    dict = {"word": 0}
    for word in words:
        if !(dict[word]):
            dict[word] = 0
        dict[word] += 1
    return dict

if __name__ == '__main__':
    words = open(sys.argv[1], "r").read().split()
    print(histogram(words))
