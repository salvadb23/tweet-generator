from flask import Flask, render_template
import random
from sample import sample
from dictionary_words import get_words, random_word_sentence

app = Flask(__name__)

@app.route('/')
def tweet():
    wordList = get_words('1984.txt')
    sentence = random_word_sentence(random.randint(10,20), wordList)
    return render_template("index.html", sentence = sentence)
