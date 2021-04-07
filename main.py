import random
import sys

from Constants import Constants
from Population import Population


class GeneticAlgorithm:
    constants = Constants()
    population_object = Population()

    def mutation(self, x):
        tmp_word = list(x.word)
        tmp_word[random.randint(0, len(x.word) - 1)] = random.choice(self.constants.all_chars)
        x.word = "".join(tmp_word)
        x.fitness = self.population_object.fitness(x.word)

    def run(self):

        loop = True
        local_generations = 0

        # STEP 1 - generate a random population
        self.population_object.generate(self.constants.population_number)

        while local_generations < self.constants.generations and loop:
            population_list = self.population_object.get_population()

            i = 0
            for k in range(int(len(population_list) / 2)):
                # STEP 2 - the evolution of the species (with mutation if needed)
                new_i = self.population_object.crossover(population_list[i], population_list[i + 1])
                r = random.random()

                if r > self.constants.mutation_threshold:
                    self.mutation(new_i)

                self.population_object.population.append(new_i)
                i = i + 2

            # STEP 3 - remove all members that are not fitting the solution
            self.population_object.natural_selection()

            best_individual = self.population_object.get_population()[0]

            # STEP 4 - exit condition
            if best_individual.fitness == 0:
                loop = False

            print('\r' + best_individual.word, end='', flush=True)

            local_generations = local_generations + 1


runner = GeneticAlgorithm()
runner.run()
