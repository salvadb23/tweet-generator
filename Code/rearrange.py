import sys
import random

del(sys.argv[0])

random.shuffle(sys.argv)

print(' '.join(sys.argv))
