from flask import Flask
import random
import frequency_analysis as freq
app = Flask(__name__)

@app.route('/')
def main():
    random_sentence = []
    hist = freq.histogram("artofwar.txt")
    total = freq.unique_words(hist)

    for i in range(random.randint(5,9)):
        random_sentence.append(freq.weighted_random(hist, total))

    random_sentence = ' '.join(random_sentence)
    return random_sentence + "."
