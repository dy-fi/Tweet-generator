import sys

def histogram(words):
    wordlists = []
    for word in words:
        if word not in wordlists:
            wordlists.append((word, words.count(word)));
    return wordlists

if __name__ == '__main__':
    words = open(sys.argv[1], "r").read().split()
    print(histogram(words))
