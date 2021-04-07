class Individual:
    word = ''
    fitness = 4

    def __init__(self, word, fitness):
        self.word = word
        self.fitness = fitness

    def __repr__(self):
        return '(' + self.word + ',' + str(self.fitness) + ')'

