from random import uniform
from dictionary_histogram import total_hist_count
from dictionary_histogram import dict_histogram
from dictionary_words import getWords

def sample(hist):
    num = 0
    random_num = uniform(0,total_hist_count(hist))
    for word in hist:
        count = hist[word]
        num += count
        if num > random_num:
            return word

if __name__ == "__main__":
    word_list = getWords('fish.txt')
    word_hist = dict_histogram(word_list)
    # print(sample(word_hist))
    probability = []
    for _ in range(0,10):
        probability.append(sample(word_hist))
    print(word_hist)
    print(dict_histogram(probability))
        
