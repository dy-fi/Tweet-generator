from dictogram import Dictogram
from collections import Counter
import random
import frequency_analysis as freq
import sys

class Markov(dict):
    def __init__(self, words, order=2):
        super(Markov, self).__init__()

        self.words = words
        self.order = order
        self.chain = None

        # holds the chain to be used as an object
        if self.chain == None:
            print("Building chain with the given corpus...")
            self.chain = self._build(words)


    def _build(self, words):
        for i in range(len(words) - self.order):
            # current window
            curr = (words[i], words[i + self.order])
            # context
            next = words[i + self.order]
            # if the window is not already in the chain
            if curr not in self:
                # learn this token by making it a histogram
                self[curr] = Dictogram(next)
            self[curr].add_count(next)
        return self

    def sentence(self):
        # empty sentence list
        random_sentence = []
        # tokens
        total = len(self.words)
        # vanilla histogram of words
        hist = freq.histogram_from_words(self.words)
        # initialize last word for the sentence contenxt
        last = ""
        # context
        window = []

        num_words = random.randint(5,9)
        for i in range(num_words):
            if len(random_sentence) == 0:
                # get the first word
                start = freq.weighted_random(hist, total)
                # list to store the start token histogram
                start_list = []

                # append it to the sentence and window
                random_sentence.append(start)
                window.append(start)

                # gets all keys that match the start token and append them to the start histogram
                for i in self.keys():
                    if i in start:
                        start_list.append(i)

                # randomly chooses words to add to the initiatial window up to the order
                for _ in range(self.order):
                    context = random.choice(start_list)
                    random_sentence.append(context)
                    window.append(context)



            window_key = tuple(window)
            last_histogram = self[window_key]
            word = freq.weighted_random(last_histogram, total)
            window.append(word)
            window.pop(0)
            # last = word
            random_sentence.append(word)


        return ' '.join(random_sentence)

# collect words
def get_words(file):
    try:
        with open(file, 'r') as f:
            words = f.read().split()
            return words
    except:
        print("Couldn't collect corpus")

# module
if __name__ == "__main__":
    words = sys.argv[1]
    chain = Markov(get_words(words), 2)
    print("Getting sentence...")
    print(chain.sentence())
