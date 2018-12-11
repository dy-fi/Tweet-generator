from dictogram import Dictogram
from collections import Counter
import frequency_analysis as freq
import sys

class Markov(dict):
    def __init__(self, words, order=2):
        super(Markov, self).__init__()

        self.order = order

        # holds the chain to be used as an object
        self.chain = self._build(words)


    def _build(self, words):
        for i in range(len(words) - self.order):
            # current window
            curr = words[i:i + self.order]
            # context
            next = words[i + self.order]
            # if the window is not already in the chain
            if curr not in self:
                # learn this token by making it a histogram
                self[current] = Dictogram(next)
            self[current].add_count(next)

    def sentence(self):
        random_sentence = []
        # tokens
        total = freq.unique_words(hist)
        # TODO implement start/stop tokens
        for i in range(random.randint(5,9)):
            random_sentence.append(freq.weighted_random(self.chain, total))
        return random_sentence

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
    print("Learning corpus...")
    chain = Markov(get_words(words), 2)
    print("Getting sentence...")
    print(chain.sentence())
