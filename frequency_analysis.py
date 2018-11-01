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
    checked = []
    count = 0
    for word in histogram:
        if word not in checked:
            checked.append(word)
            count += 1
    return count

def frequency(word, histogram):
    return histogram[word]

def randomWord(histogram):
    return random.choice(histogram)

# slow
def freqWeightRandom(histogram):
    weightList = []
    for word in histogram:
        for i in range(histogram[word]):
            weightList.append(word)
    return random.choice(weightList)

# much faster
def freqWeightRandom2(histogram):
    destination = random.randint(0, len(histogram))
    for word in histogram:
        destination = destination - histogram[word]
        if destination < 0:
            return word

count = 1000
newList = []
while(count > 0):
    newList.append(freqWeightRandom2(histogram("artofwar.txt")))
    count = count - 1
print(newList)
