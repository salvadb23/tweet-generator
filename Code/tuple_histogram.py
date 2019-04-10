from dictionary_words import getWords
from dictionary_histogram import dict_histogram
wordList = getWords('animals.txt')

def histogram_tuple(list):
    dictionary = dict_histogram(list)
    tuple_histogram = []
    for i in dictionary:
        tuple_histogram.append((i, dictionary[i]))
    return tuple_histogram

if __name__ == "__main__":
    print(histogram_tuple(wordList))
