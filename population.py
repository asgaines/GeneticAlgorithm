import random

from organism import Organism


class Population():
    organisms = []
    num_children = 4

    def __init__(self, target, num_organisms, organisms=None):
        self.target = target
        self.num_organisms = num_organisms
        self.num_generations = 0
        if organisms is None:
            self.organisms = [Organism(len(self.target)) for _ in range(num_organisms)]
        else:
            self.organisms = organisms
        self.sort_organisms()

    def generation(self):
        self.organisms = self.mate()
        self.sort_organisms()
        self.num_generations += 1

    def target_achieved(self):
        return self.fittest.DNA == self.target

    def sort_organisms(self):
        self.organisms = sorted(self.organisms, key=lambda organism: organism.get_fitness(self.target), reverse=True)

    def mate(self):
        # Only fittest half mate
        next_gen = []
        for i in range(0, int(self.num_organisms / 2) + 1, 2):
            for _ in range(self.num_children):
                next_gen.append(self.organisms[i].create_offspring(self.organisms[i + 1]))
        return next_gen[:self.num_organisms]
            
    @property
    def fittest(self):
        # Organisms must be sorted
        return self.organisms[0]
