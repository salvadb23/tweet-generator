from flask import Flask, render_template
import random
from sample import sample
from dictionary_words import get_words, random_word_sentence
from higher_markov import MarkovChain

app = Flask(__name__)

@app.route('/')
def tweet():
    word_list = get_words('1984.txt')
    markov_chain = MarkovChain(word_list)
    sentence = markov_chain.chain_traversal(30)
    return render_template("index.html", sentence = sentence)
