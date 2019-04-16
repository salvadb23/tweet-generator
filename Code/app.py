from flask import Flask, render_template
import random
from sample import sample
from dictionary_words import getWords, randomWordSentence

app = Flask(__name__)

@app.route('/')
def hello_world():
    wordList = getWords('1984.txt')
    sentence = randomWordSentence(random.randint(10,20), wordList)
    return render_template("index.html", sentence = sentence)
