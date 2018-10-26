import sys

def histogram(words):
    wordlists = []
    for word in words:
        if word not in wordlists:
            wordlists.append([word, 1])
        for item in wordlists:
            if item[0] == word:
                item[1] += 1
    return wordlists

filename = sys.argv[1]
words = open(sys.argv[1], "r").read().split()
print(histogram(words))
