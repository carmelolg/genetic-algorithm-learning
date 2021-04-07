from Constants import Constants
from Population import Population


class GeneticAlgorithm:
    constants = Constants()

    def run(self):

        loop = True
        local_generations = 0

        population = Population()
        population.generate(self.constants.population_number)

        while local_generations < self.constants.generations and loop:
            population_list = population.get_population()

            i = 0
            for k in range(int(len(population_list) / 2)):
                population.crossover(population_list[i], population_list[i + 1])
                i = i + 2

            population.natural_selection()

            best_individual = population.get_population()[0]

            local_generations = local_generations + 1

            if best_individual.fitness == 0:
                print(best_individual.word)
                loop = False
            else:
                print(best_individual, "still not the best")


runner = GeneticAlgorithm()
runner.run()
