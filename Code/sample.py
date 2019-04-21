from random import uniform
from dictionary_histogram import total_hist_count
from dictionary_histogram import dict_histogram
from dictionary_words import get_words
from pprint import pprint
import sys

def sample(hist):
    num = 0
    random_num = uniform(0,total_hist_count(hist))
    for word in hist:
        count = hist[word]
        num += count
        if num > random_num:
            return word

def sample_sentence(num, hist):
    """ using the sample function, this function creates a sentence,
     the length depending on what is passed into num """
     
    sentence = []
    for _ in range(0,num):
        sentence.append(sample(hist))
    return ' '.join(sentence)

def test_probability(word_hist, num):
    probability = []
    for _ in range(0,num):
        probability.append(sample(word_hist))
    pprint(dict_histogram(probability))

if __name__ == "__main__":
    word_list = get_words('fish.txt')
    word_hist = dict_histogram(word_list)
    test_probability(word_hist, 1000)
