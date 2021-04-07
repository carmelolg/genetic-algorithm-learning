import random
from string import ascii_letters

from Constants import Constants
from Individual import Individual


class Population:

    population = []
    constants = Constants()

    def get_population(self):
        return self.population

    def sort(self):
        self.population.sort(key=lambda x: x.fitness)

    def generate(self, n):
        for i in range(n):
            word_generated = ''
            for j in range(self.constants.max_length):
                word_generated = word_generated + random.choice(ascii_letters + ' ')
            self.population.append(Individual(word_generated))

    def crossover(self, x, y):

        word_x = x.word
        word_y = y.word
        half = int(self.constants.max_length / 2)

        new = word_x[:half] + word_y[half:]

        new_i = Individual(new)
        r = random.random()

        if r > self.constants.mutation_threshold:
            new_i.mutation()

        self.population.append(new_i)

    def natural_selection(self):
        self.sort()
        self.population = self.population[:self.constants.population_number]
