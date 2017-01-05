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

    def create_offspring(self, partner):
        # Determine crossover points
        crossover_indices = self._get_crossover_indices()
        # Join parents DNA, part from each cut at crossover point
        offspring_DNA = self._splice_DNA(partner, crossover_indices)
        # Expose DNA to mutation possibility
        offspring_DNA = ''.join([nucleotide if random.random() > self.mutation_rate else random.choice(self.nucleotides) for nucleotide in offspring_DNA])
        return Organism(len(self.DNA), offspring_DNA)
    
    def get_fitness(self, target):
        return sum([1 for i, character in enumerate(target) if character == self.DNA[i]])

    def _get_crossover_indices(self):
        return [i for i in range(len(self.DNA)) if random.random() < config.values['crossover_rate']]
    
    def _splice_DNA(self, partner, indices):
        strand1 = self.DNA
        strand2 = partner.DNA
        for index in indices:
            strand1, strand2 = strand1[:index] + strand2[index:], strand2[:index] + strand1[index:]
        return random.choice([strand1, strand2])

    def _mutate_DNA(self, DNA):
        return ''.join([nucleotide if random.random() > self.mutation_rate else random.choice(self.nucleotides) for nucleotide in DNA])
