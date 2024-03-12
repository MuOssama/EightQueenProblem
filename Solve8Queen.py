import random

def solve_queens(initial_board, population_size, mutation_rate, max_generations):
    def fitness(chromosome):
        clashes = 0
        for i in range(len(chromosome)):
            for j in range(i + 1, len(chromosome)):
                if chromosome[i] == chromosome[j] or abs(i - j) == abs(chromosome[i] - chromosome[j]):
                    clashes += 1
        return 28 - clashes  # Max fitness is 28 (no clashes)

    def crossover(parent1, parent2):
        crossover_point = random.randint(1, 7)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(chromosome, mutation_rate):
        for i in range(len(chromosome)):
            if random.random() < mutation_rate:
                chromosome[i] = random.randint(0, 7)
        return chromosome

    population = []
    for _ in range(population_size):
        chromosome = initial_board.copy()
        population.append(chromosome)

    generation = 0
    while generation < max_generations:
        population.sort(key=fitness, reverse=True)
        if fitness(population[0]) == 28:  # Found the solution
            return population[0]
        new_population = [population[0]]  # Elitism: keep the best chromosome
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
        generation += 1
    return None  # Failed to find a solution within max generations

# Example usage
initial_board = [5, 1, 2, 3, 4, 5, 6, 7]  # Initial queen positions for each column
solution = solve_queens(initial_board, population_size=100, mutation_rate=0.01, max_generations=10000)
if solution:
    print("Found solution:", solution)
else:
    print("Failed to find a solution.")