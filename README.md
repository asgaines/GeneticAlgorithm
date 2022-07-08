# Genetic Algorithm

Implementation of a genetic algorithm to generate a result which matches the target string following successive generations. 

## Algorithm

A set number of organisms, with DNA representing a guess at target sequence, are first randomly generated. The top half of organisms, determined by fitness score from number of matches, are mated with one another to create the next generation until one matches the target sequence. Child DNA is determined from crossovers of 2 parent DNA strands (determined by `crossover_rate`) and is then exposed to possible mutations (determined by `mutation_rate`).

## Run Program

- `git clone https://github.com/asgaines/GeneticAlgorithm GeneticAlgorithm`
- `cd GeneticAlgorithm`
- `docker build -t genalgo .`
- `docker run -it --rm -v $PWD:/usr/src/app --name genalgo_run genalgo`

### Command Line Usage

Add command line arguments to end of `docker run` command. Example:

`docker run -it --rm -v $PWD:/usr/src/app --name genalgo_run genalgo -t "GATCAGCATGAC"`

```
usage: main.py [-h] [-t TARGET] [-p NUM_POPULATION] [-m MUTATION_RATE] [-c CROSSOVER_RATE]

Genetic algorithm to find optimal solution in large search space

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target solution to optimize for
  -p NUM_POPULATION, --num_population NUM_POPULATION
                        Number of organisms in population
  -m MUTATION_RATE, --mutation_rate MUTATION_RATE
                        Rate [0-1] of point mutation when creating new generation
  -c CROSSOVER_RATE, --crossover_rate CROSSOVER_RATE
                        Rate [0-1] of likelihood of crossover event at a locus when creating a new generation
```


## Results

Number of generations and time to evolve to target sequence is printed at completion. To see most fit organism of each generation, uncomment line in `main.py`.

Average number of generations (10 trials) is 995 in 6.012119 seconds with the following config values:
- `target: Verily the lust for comfort murders the passion of the soul, and then walks grinning in the funeral.`
- `num_population: 100`
- `mutation_rate: 0.01`
- `crossover_rate: 0.1`

## Testing

- `mocker run -it --rm --name genalgo_run --entrypoint="python" genalgo -m unittest`
