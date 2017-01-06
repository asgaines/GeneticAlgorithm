import unittest

from population import Population
from organism import Organism


class OrganismTests(unittest.TestCase):
    def setUp(self):
        self.target = 'Persevere'
        self.num_organisms = 5
        self.population = Population(self.target, self.num_organisms)

    def test_random_population_has_proper_DNA_length(self):
        target = 'ATGCA'
        pop = Population(target, 10)

        for organism in pop.organisms:
            self.assertEqual(len(organism.DNA), len(target))

    def test_correct_fittest_organism_chosen(self):
        target = 'AAAAA'
        organisms = [
            Organism(len(self.target), 'XXXXX'),
            Organism(len(self.target), 'AXXXX'),
            Organism(len(self.target), 'AAXXX'),
            Organism(len(self.target), 'AAAXX'),
            # Highest score:
            Organism(len(self.target), 'AAAAX'),
        ]
        pop = Population(target, len(organisms), organisms)
        self.assertEqual(pop.fittest, organisms[-1])

    def test_order_organisms_orders_correctly(self):
        target = 'abc'
        organisms = [
            # Ascending order
            Organism(len(target), 'XXX'),
            Organism(len(target), 'aXX'),
            Organism(len(target), 'abX'),
        ]
        pop = Population(target, len(organisms), organisms)
        pop.sort_organisms()
        self.assertEqual(pop.organisms, organisms[::-1])

    def test_mating_event_maintains_same_population_num(self):
        self.assertEqual(len(self.population.mate()), self.num_organisms)

    def test_target_achieved_when_organism_matches_target(self):
        target = 'Answer'
        organisms = [
            Organism(len(target), 'XXXXXX'),
            Organism(len(target), 'Answer'),
        ]
        pop = Population(target, len(organisms), organisms)
        self.assertTrue(pop.target_achieved())

    def test_target_not_achieved_when_no_organism_matches_target(self):
        target = 'Answer'
        organisms = [
            Organism(len(target), 'XXXXXX'),
            Organism(len(target), 'YYYYYY'),
        ]
        pop = Population(target, len(organisms), organisms)
        self.assertFalse(pop.target_achieved())

    def test_new_generation_increments_num_generation(self):
        num_generations_start = self.population.num_generations
        self.population.generation()
        self.assertEqual(self.population.num_generations, num_generations_start + 1)
