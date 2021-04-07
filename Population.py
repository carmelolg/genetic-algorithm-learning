import random
from string import ascii_letters

import textdistance

from Constants import Constants
from Individual import Individual


class Population:

    population = []
    constants = Constants()

    def get_population(self):
        return self.population

    def fitness(self, word):
        return textdistance.hamming(word, self.constants.solution)

    # Never used in this case
    def perform_fitness(self, x):
        x.fitness = self.fitness(x.word)

    # Never used in this case
    def population_fitness(self):
        self.population = map(lambda x: self.perform_fitness(x), self.population)

    def sort(self):
        self.population.sort(key=lambda x: x.fitness)

    def generate(self, n):
        for i in range(n):
            word_generated = ''
            for j in range(self.constants.max_length):
                word_generated = word_generated + random.choice(ascii_letters + ' ')
            self.population.append(Individual(word_generated, self.fitness(word_generated)))

    def mutation(self, x):
        tmp_word = list(x.word)
        tmp_word[random.randint(0, len(x.word) - 1)] = random.choice(ascii_letters + ' ')
        x.word = "".join(tmp_word)
        x.fitness = self.fitness(x.word)

    def crossover(self, x, y):

        word_x = x.word
        word_y = y.word
        half = int(self.constants.max_length / 2)

        new = word_x[:half] + word_y[half:]

        new_i = Individual(new, self.fitness(new))
        r = random.random()

        if r > self.constants.mutation_threshold:
            self.mutation(new_i)

        self.population.append(new_i)

    def natural_selection(self):
        self.sort()
        self.population = self.population[:self.constants.population_number]
