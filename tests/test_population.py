import unittest

from population import Population
from organism import Organism


class OrganismTests(unittest.TestCase):
    def setUp(self):
        self.target = 'Persevere'
        self.num_population = 5
        self.organisms = [Organism(0.01, 0.1, len(self.target)) for _ in range(self.num_population)]
        self.population = Population(self.target, self.organisms)

    def test_random_population_has_proper_DNA_length(self):
        target = 'ATGCA'
        organisms = [Organism(0.01, 0.1, len(target)) for _ in range(10)]
        pop = Population(target, organisms)

        for organism in pop.organisms:
            self.assertEqual(len(organism.DNA), len(target))

    def test_correct_fittest_organism_chosen(self):
        target = 'AAAAA'
        organisms = [
            Organism(0.01, 0.1, len(self.target), 'XXXXX'),
            Organism(0.01, 0.1, len(self.target), 'AXXXX'),
            Organism(0.01, 0.1, len(self.target), 'AAXXX'),
            Organism(0.01, 0.1, len(self.target), 'AAAXX'),
            # Highest score:
            Organism(0.01, 0.1, len(self.target), 'AAAAX'),
        ]
        pop = Population(target, organisms)
        self.assertEqual(pop.fittest, organisms[-1])

    def test_order_organisms_orders_correctly(self):
        target = 'abc'
        organisms = [
            # Ascending order
            Organism(0.01, 0.1, len(target), 'XXX'),
            Organism(0.01, 0.1, len(target), 'aXX'),
            Organism(0.01, 0.1, len(target), 'abX'),
        ]
        pop = Population(target, organisms)
        pop.sort_organisms()
        self.assertEqual(pop.organisms, organisms[::-1])

    def test_mating_event_maintains_same_population_num(self):
        self.assertEqual(len(self.population.mate()), self.num_population)

    def test_target_achieved_when_organism_matches_target(self):
        target = 'Answer'
        organisms = [
            Organism(0.01, 0.1, len(target), 'XXXXXX'),
            Organism(0.01, 0.1, len(target), 'Answer'),
        ]
        pop = Population(target, organisms)
        self.assertTrue(pop.target_achieved())

    def test_target_not_achieved_when_no_organism_matches_target(self):
        target = 'Answer'
        organisms = [
            Organism(0.01, 0.1, len(target), 'XXXXXX'),
            Organism(0.01, 0.1, len(target), 'YYYYYY'),
        ]
        pop = Population(target, organisms)
        self.assertFalse(pop.target_achieved())

    def test_new_generation_increments_num_generation(self):
        num_generations_start = self.population.num_generations
        self.population.generation()
        self.assertEqual(self.population.num_generations, num_generations_start + 1)
