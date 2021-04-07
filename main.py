import random
from string import ascii_letters

import nltk

population_number = 10
mutation_threshold = 0.18
max_length = 4
solution = 'ciao'


class Individual:
    word = ''
    fitness = 0

    def __init__(self, word):
        self.word = word
        self.fitness = self.distance()

    def __repr__(self):
        return '(' + self.word + ',' + str(self.fitness) + ')'

    def distance(self):
        return nltk.edit_distance(self.word, solution)

    def mutation(self):
        #print('I must mutate ', self.word)
        tmp_word = list(self.word)
        tmp_word[random.randint(0, len(self.word) - 1)] = random.choice(ascii_letters)
        self.word = "".join(tmp_word)


class Population:
    population = []
    new_population = []

    def get_population(self):
        return self.population

    def sort(self):
        #print(self.population)
        self.population.sort(key=lambda x: x.fitness, reverse=False)

    def generate(self, n):
        for i in range(n):
            word_generated = ''
            for j in range(max_length):
                word_generated = word_generated + random.choice(ascii_letters)
            self.population.append(Individual(word_generated))

    def crossover(self, x, y):

        word_x = x.word
        word_y = y.word
        half = int(max_length / 2)

        new = word_x[:half] + word_y[half:]

        new_i = Individual(new)
        r = random.random()

        if r > mutation_threshold:
            new_i.mutation()

        self.new_population.append(new_i)

    def mergePopulation(self):
        self.population = self.new_population


loop = True
population = Population()
population.generate(population_number)
#print(population.get_population())
population.sort()

while (loop):
    population_list = population.get_population()
    #print(population.get_population())

    i = 0
    for k in range(int(len(population_list) / 2)):
        population.crossover(population_list[i], population_list[i + 1])
        i = i + 2

    population.mergePopulation()
    population.sort()

    best_individual = population.get_population()[0]

    if best_individual.fitness == 0:
        print(best_individual.word)
        loop = False
    else:
        print(best_individual, "still not the best")
