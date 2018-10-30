import sys

def histogram(words):
    """
        Takes an argument(corpus) and returns the times each word is used
    """
    wordlists = []
    for word in words:
        if word not in wordlists:
            wordlists.append([word, 1])
        for item in wordlists:
            if item[0] == word:
                item[1] += 1
    return wordlists

if __name__ == '__main__':
    words = open(sys.argv[1], "r").read().split()
    print(histogram(words))
