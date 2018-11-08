import profile
import random
from collections import Counter


def histogram(source_text):
"""
    Takes an argument(file) and returns the times each word is used
"""
    words = open(source_text, "r").read().split()
    histogram = Counter()
    for word in words:
        histogram[word] += 1
    return histogram

def unique_words(histogram):
    return sum(histogram.values())

def frequency(word, histogram):
    return histogram[word]

def random_word(histogram):
    return random.choice(histogram)

# # slow  O(n^2) and stores a list the size of the original corpus
# def freqWeightRandom(histogram):
#     weightList = []
#     for word in histogram:
#         for i in range(histogram[word]):
#             weightList.append(word)
#     return random.choice(weightList)

# much faster O(n) and stores 1 int
def weighted_random(histogram, total):
"""
    Takes a histogram and returns a weighted random choice from it
"""
    destination = random.randint(0, total)
    for word in histogram:
        destination = destination - histogram[word]
        if destination < 0:
            return word

# modularity
if __name__ == "__main__":
    art_of_war = histogram("artofwar.txt")
    total = unique_words(art_of_war)
    count = 10000
    newList = []
    while(count > 0):
        newList.append(weighted_random(art_of_war, total))
        count = count - 1
    print(newList)
