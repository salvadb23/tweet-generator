from dictionary_words import get_words
from pprint import pprint
import random
from sample import sample


class MarkovChain(dict):
    '''A Markov Chain Generator'''

    def __init__(self, word_list):
        '''Inits the Markov Chain'''
        super(MarkovChain, self).__init__()
        self.word_list = word_list

        self.tokens = 0
        self.types = 0

        if word_list is not None:
            self.create_chain(word_list)

    def create_chain(self, word_list):
        '''Build the Markov Chain from a word_list'''
        for index in range(len(self.word_list)-1):
            current_word = self.word_list[index]
            # Gets the word next to current word
            next_word = self.word_list[index + 1]
            if current_word in self:
                if next_word in self[current_word]:
                    self[current_word][next_word] += 1
                else:
                    self[current_word][next_word] = 1
            else:
                self[current_word] = {next_word: 1}
        return self

    def chain_traversal(self, length=10):
        ''' Creates a sentence using the Markov Chain'''
        current_word = random.choice(list(self))
        sentence = []
        sentence.append(current_word)
        for _ in range(length):
            new_word = sample(self[current_word])
            sentence.append(sample(self[current_word]))
            current_word = new_word
        return ' '.join(sentence)


def test_chain_traversal():
    word_list = get_words("1984.txt")
    markov_chain = MarkovChain(word_list)
    for _ in range(5):
        pprint(markov_chain.chain_traversal(10))


def main():

    test_chain_traversal()


if __name__ == "__main__":
    main()
