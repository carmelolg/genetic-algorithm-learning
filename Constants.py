from string import ascii_letters


class Constants:
    population_number = 1000
    mutation_threshold = 0.18
    solution = 'I\'m produced by a genetic algorithm!'
    #solution = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    max_length = len(solution)
    generations = 50000
    all_chars = ascii_letters + ' \'!?*&.;,-'
