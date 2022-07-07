from typing import List

from organism import Organism


class Population():
    num_children = 4

    def __init__(self, target: str, organisms: List[Organism]=None):
        self.target = target
        self.organisms = organisms
        self.num_generations = 0

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
        midpoint = int(len(self.organisms) / 2) + 1

        for i in range(0, midpoint, 2):
            for _ in range(self.num_children):
                next_gen.append(self.organisms[i].create_offspring(self.organisms[i + 1]))

        return next_gen[:len(self.organisms)]
            
    @property
    def fittest(self):
        # Organisms must be sorted
        return self.organisms[0]
