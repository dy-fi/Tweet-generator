import profile
import random
from collections import Counter

def unique_words(histogram):
    return sum(histogram.values())

def frequency(word, histogram):
    return histogram[word]

def random_word(histogram):
    return random.choice(histogram)


def histogram(source_text):
    """
    Takes an argument(file) and returns the times each word is used
    """

    words = open(source_text, "r").read().split()
    histogram = Counter()
    for word in words:
        histogram[word] += 1
    return histogram


# O(n) and stores 1 int
def weighted_random(histogram, total):
    """
    Takes a histogram and returns a weighted random choice from it
    """

    destination = random.randint(0, total)
    for word in histogram:
        destination = destination - histogram[word]
        if destination < 0:
            return word


def execute(hist):
    """
    Called if file is executed as a standalone script
    """

    art_of_war = histogram("artofwar.txt")
    newList = []
    for i in range(random.randint(5,9)):
        newList.append(weighted_random(art_of_war, unique_words(art_of_war)))
    return ' '.join(newList) + '.'


# modularity
if __name__ == "__main__":
    print(execute(histogram("artofwar.txt")))
