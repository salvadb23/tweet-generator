import random
import sys
import time

def getWords(file):
    words = open(file, 'r')
    wordList = words.read().split()
    words.close()
    return wordList

def randomWordSentence(num, wordList):
    sentence = []
    while len(sentence) < num:
        sentence.append(wordList[random.randint(1,len(wordList))])
    return ' '.join(sentence)

if __name__ == '__main__':
    start = time.time()
    file = '/usr/share/dict/words'
    print(randomWordSentence(int(sys.argv[1],), getWords(file)))
    end = time.time()
    print(end-start)


# print(end - start)
