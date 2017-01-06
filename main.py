import random
from datetime import datetime

import config
from organism import Organism
from population import Population


if __name__ == '__main__':
    start = datetime.now()

    population = Population(
        target=config.values['target'],
        num_organisms=config.values['num_population']
    )

    while not population.target_achieved():
        population.generation()
        # Uncomment the following to see the results in real time
        print('#{0} (score: {1}): {2}'.format(population.num_generations, population.fittest.get_fitness(config.values['target']), population.fittest.DNA).encode('unicode-escape'))
    print('{0} generations in {1}'.format(population.num_generations, datetime.now() - start))
