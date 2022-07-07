import unittest

from organism import Organism


class OrganismTest(unittest.TestCase):
    def setUp(self):
        self.target = '''Believe you can and you're halfway there.'''
        self.organism = Organism(0.01, 0.1, len(self.target))

    def test_DNA_length_initialized_to_target_length(self):
        self.assertEqual(len(self.target), len(self.organism.DNA))

    def test_init_organism_with_DNA_properly_set(self):
        DNA = 'GATTACA'
        new_organism = Organism(0.01, 0.1, len(DNA), DNA)
        self.assertEqual(new_organism.DNA, DNA)

    def test_fitness_returns_0_if_no_overlap(self):
        target = 'Stay golden'
        organism = Organism(0.01, 0.1, len(target), 'Golden stay')
        self.assertEqual(organism.get_fitness(target), 0)

    def test_fitness_returns_1_if_1_overlap(self):
        target = 'Indigo'
        organism = Organism(0.01, 0.1, len(target), 'Import')
        self.assertEqual(organism.get_fitness(target), 1)

    def test_fitness_returns_length_of_target_if_correct(self):
        target = 'The years teach much the days never know.'
        organism = Organism(0.01, 0.1, len(target), target)
        self.assertEqual(organism.get_fitness(target), len(target))

    def test_create_offspring_has_same_length_DNA(self):
        organism1 = Organism(0.01, 0.1, 10, 'ABCDEFGHIJ')
        organism2 = Organism(0.01, 0.1, 10, 'JIHGFEDCBA')
        child = organism1.create_offspring(organism2)
        self.assertEqual(len(organism1.DNA), len(organism2.DNA))

    def test_splice_of_DNA_with_one_crossover_returns_proper_sequence(self):
        index = [3]
        organism1 = Organism(0.01, 0.1, 6, 'XXXXXX')
        organism2 = Organism(0.01, 0.1, 6, 'YYYYYY')
        self.assertIn(organism1._splice_DNA(organism2, index), ['XXXYYY', 'YYYXXX'])

    def test_splice_of_DNA_with_multiple_crossovers_returns_proper_sequence(self):
        index = [1, 3]
        organism1 = Organism(0.01, 0.1, 6, 'AAAAAA')
        organism2 = Organism(0.01, 0.1, 6, 'ZZZZZZ')
        self.assertIn(organism1._splice_DNA(organism2, index), ['AZZAAA', 'ZAAZZZ'])

    def test_crossover_indices_generated_every_index_if_rate_is_1(self):
        organism = Organism(0.01, 1, 5, 'ATGCA')
        self.assertEqual(organism._get_crossover_indices(), list(range(len(organism.DNA))))

    def test_crossover_indices_generated_none_if_rate_is_0(self):
        organism = Organism(0.01, 0, 5, 'ATGCA')
        self.assertEqual(organism._get_crossover_indices(), [])

    def test_no_mutations_if_rate_is_0(self):
        DNA = 'One fish, two fish, red fish, blue fish'
        organism = Organism(0, 0.1, 5, 'ATGCA')
        self.assertEqual(organism._mutate_DNA(DNA), DNA)

    def test_DNA_mutates_if_rate_is_1(self):
        DNA = 'The longer this is, the less likely it will be mutated back to itself. Chances are 1 in (len(string.printable) raised to the length of this DNA)'
        organism = Organism(1, 0.1, 5, 'ATGCA')
        self.assertNotEqual(organism._mutate_DNA(DNA), DNA)

