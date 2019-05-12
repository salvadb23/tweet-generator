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
        for index in range(len(self.word_list)-2):
            prev_2 = (self.word_list[index], self.word_list[index + 1])
            # Gets the word next to current word
            next_word = self.word_list[index + 2]
            if prev_2 in self:
                if next_word in self[prev_2]:
                    self[prev_2][next_word] += 1
                else:
                    self[prev_2][next_word] = 1
            else:
                self[prev_2] = {next_word: 1}
        return self

    def chain_traversal(self, length=20):
        ''' Creates a sentence using the Markov Chain'''
        current_word = random.choice(list(self.keys()))
        sentence = []
        for _ in range(length):
            new_word = sample(self[current_word])
            sentence.append(current_word[1])
            current_word = (current_word[1],new_word)
        return ' '.join(sentence)


def test_chain_traversal():
    word_list = get_words("1984.txt")
    markov_chain = MarkovChain(word_list)
    pprint(markov_chain.chain_traversal())


def main():

    test_chain_traversal()


if __name__ == "__main__":
    main()
