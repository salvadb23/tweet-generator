import sys
import random

def shuffleArr(arr):
    copyArr = arr.copy()
    random.shuffle(copyArr)
    shuffledArr = copyArr
    return shuffledArr

if __name__ == '__main__':
    arr = sys.argv[1:]
    print(' '.join(shuffleArr(arr)))
