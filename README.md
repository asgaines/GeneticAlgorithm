# Genetic Algorithm

Implementation of a genetic algorithm to generate a result which matches the target string following successive generations. 

## Algorithm

A set number of organisms, with DNA representing a guess at target sequence, are first randomly generated. The top half of organisms, determined by fitness score from number of matches, are mated with one another to create the next generation until one matches the target sequence. Child DNA is determined from a crossover of 2 parent DNA strands and is then exposed to possible mutations.

## Run Program

- `git clone https://github.com/asgaines/GeneticAlgorithm GeneticAlgorithm`
- `cd GeneticAlgorithm`
- `python main.py`

Alter values in `config.py` for modified behavior and optimization.

## Results

Number of generations and time to evolve to target sequence is printed at completion. To see most fit organism of each generation, uncomment line in `main.py`.

Average number of generations (10 trials) is 1952 with the following config values:
- `target: Verily the lust for comfort murders the passion of the soul, and then walks grinning in the funeral.`
- `num_population: 100`
- `mutation_rate: 0.01`

