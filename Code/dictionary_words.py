import random
import sys

words = open('/usr/share/dict/words', 'r')
wordList = words.read().split()

def randomWords(num):
    randomWordList = []
    while len(randomWordList) < num:
        randomWordList.append(wordList[random.randint(1,len(wordList))])
    return ' '.join(randomWordList)

print(randomWords(int(sys.argv[1])))
