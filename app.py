from flask import Flask
import random
import markov
import frequency_analysis as freq

app = Flask(__name__)

@app.route('/')
def main():
    random_sentence = []
    words = open('artofwar.txt', "r").read().split()
    hist = markov.dictogram(words)
    total = hist.tokens

    for i in range(random.randint(5,9)):
        random_sentence.append(freq.weighted_random(hist, total))

    random_sentence = ' '.join(random_sentence) + "."
    # return render_template('index.html', sentence = random_sentence)
    return random_sentence
