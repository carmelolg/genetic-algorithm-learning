import random
from string import ascii_letters

import textdistance

from Constants import Constants


class Individual:
    word = ''
    fitness = 4

    constants = Constants()

    def __init__(self, word):
        self.word = word
        self.fitness = self.distance()

    def __repr__(self):
        return '(' + self.word + ',' + str(self.fitness) + ')'

    def distance(self):
        return textdistance.hamming(self.word, self.constants.solution)

    def mutation(self):
        tmp_word = list(self.word)
        tmp_word[random.randint(0, len(self.word) - 1)] = random.choice(ascii_letters + ' ')
        self.word = "".join(tmp_word)
        self.fitness = self.distance()

