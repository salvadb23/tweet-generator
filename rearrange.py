import sys
import random

def shuffleArr(arr):
    shuffleArr = arr.copy()
    random.shuffle(shuffleArr)
    return shuffleArr

if __name__ == '__main__':
    arr = sys.argv[1:]
    print(' '.join(shuffleArr(arr)))
