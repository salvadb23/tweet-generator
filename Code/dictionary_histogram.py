from dictionary_words import getWords



def dict_histogram(lists):
    """Count occurences in the given list 
    and return that data structure"""
    dictionary = {}
    for i in lists:
        if i in dictionary:
            dictionary[i] += 1
        else :
            dictionary[i] = 1

    return dictionary

if __name__ == "__main__":
    print(dict_histogram(getWords('animals.txt')))
