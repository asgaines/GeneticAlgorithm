import random

from organism import Organism


class Population():
    organisms = []

    def __init__(self, target, num_organisms):
        self.target = target
        self.num_organisms = num_organisms
        self.num_generations = 0
        for _ in range(num_organisms):
            self.organisms.append(Organism(len(self.target)))
        self.sort_organisms()

    def generation(self):
        self.organisms = self.mate()
        self.sort_organisms()
        self.num_generations += 1

    def target_achieved(self):
        return self.organisms[0].DNA == self.target

    def sort_organisms(self):
        self.organisms = sorted(self.organisms, key=lambda organism: organism.get_fitness(self.target), reverse=True)

    def mate(self):
        # Only top half mate, 4 children each
        next_gen = []
        for i in range(0, int(self.num_organisms / 2), 2):
            for _ in range(4):
                next_gen.append(self.organisms[i].create_offspring(self.organisms[i + 1]))
        return next_gen[:self.num_organisms]
            
    def get_most_fit(self):
        return self.organisms[0].DNA
