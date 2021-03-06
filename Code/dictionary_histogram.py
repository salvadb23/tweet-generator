from dictionary_words import get_words

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

def total_hist_count(hist):
    total_count = 0
    for word in hist:
        total_count += hist[word]
    return total_count
    
if __name__ == "__main__":
    print(dict_histogram(get_words('1984.txt')))
