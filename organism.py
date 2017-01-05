import random
import string

import config

class Organism():
    nucleotides = string.printable
    mutation_rate = config.values['mutation_rate']

    def __init__(self, target_length, DNA=None):
        if not DNA:
            self.DNA = ''.join([random.choice(self.nucleotides) for _ in range(target_length)])
        else:
            self.DNA = DNA

    def mate(self, partner):
        # Choose random crossover point
        crossover_index = random.randint(0, len(self.DNA) - 1)
        # Join parents DNA, part from each cut at crossover point
        offspring_DNA = self.DNA[:crossover_index] + partner.DNA[crossover_index:]
        # Expose DNA to mutation possibility
        offspring_DNA = ''.join([nucleotide if random.random() > self.mutation_rate else random.choice(self.nucleotides) for nucleotide in offspring_DNA])
        return Organism(len(self.DNA), offspring_DNA)
    
    def get_fitness(self, target):
        return sum([1 for i, character in enumerate(target) if character == self.DNA[i]])
