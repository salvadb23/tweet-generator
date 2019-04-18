import random
import sys
import time

def get_words(file):
    words = open(file, 'r')
    wordList = words.read().split()
    words.close()
    return wordList

def random_word_sentence(num, wordList):
    sentence = []
    while len(sentence) < num:
        sentence.append(wordList[random.randint(1,len(wordList))])
    return ' '.join(sentence)

if __name__ == '__main__':
    start = time.time()
    file = '/usr/share/dict/words'
    print(random_word_sentence(int(sys.argv[1],), get_words(file)))
    end = time.time()
    print(end-start)


# print(end - start)
