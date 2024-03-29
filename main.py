import argparse

from datetime import datetime
import matplotlib.pyplot as plt

from organism import Organism
from population import Population


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genetic algorithm to find optimal solution in large search space')
    parser.add_argument('-t', '--target', type=str, help='Target solution to optimize for', default='Verily the lust for comfort murders the passion of the soul, and then walks grinning in the funeral.')
    parser.add_argument('-p', '--num_population', required=False, type=int, help='Number of organisms in population', default=100)
    parser.add_argument('-m', '--mutation_rate', required=False, type=float, help='Rate [0-1] of point mutation when creating new generation', default=0.01)
    parser.add_argument('-c', '--crossover_rate', required=False, type=float, help='Rate [0-1] of likelihood of crossover event at a locus when creating a new generation', default=0.1)
    args = parser.parse_args()

    start = datetime.now()

    organisms = [Organism(args.mutation_rate, args.crossover_rate, len(args.target)) for _ in range(args.num_population)]

    population = Population(
        target=args.target,
        organisms=organisms
    )

    scores = []

    while not population.target_achieved():
        population.generation()
        gen = population.num_generations
        score = population.fittest.get_fitness(args.target)

        scores.append({
            'gen': population.num_generations,
            'score': score,
        })

        # Uncomment the following to see the results in real time
        print('#{0} (score: {1}): {2}'.format(gen, score, population.fittest.DNA).encode('unicode-escape'))

    print('{0} generations in {1}'.format(population.num_generations, datetime.now() - start))

    for score in scores:
        plt.plot(score['gen'], score['score'], 'b,')

    plt.xlabel('generation #')
    plt.ylabel('score')

    results_fname = './results.png'
    plt.savefig(results_fname)
    print(f'Score curve visualization graph written to {results_fname}')
