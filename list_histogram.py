from dictionary_words import getWords
from dictionary_histogram import dict_histogram

wordList = getWords('animals.txt')

def histogram_list(list):
    dictionary = dict_histogram(list)
    list_histogram = []
    for i in dictionary:
        list_histogram.append([i, dictionary[i]])
    return list_histogram


if __name__ == "__main__":
    print(histogram_list(wordList))
