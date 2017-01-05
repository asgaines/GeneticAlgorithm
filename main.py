import random
from datetime import datetime

import config
from organism import Organism
from population import Population

population = Population(
    target=config.values['target'],
    num_organisms=config.values['num_population']
)

if __name__ == '__main__':
    while not population.target_achieved():
        population.generation()
        # Uncomment the following to see the results in real time
        # print('{0}: {1}'.format(population.num_generations, population.get_most_fit()).encode('unicode-escape'))
    print('{0} generations in {1}'.format(population.num_generations, datetime.now() - start))
