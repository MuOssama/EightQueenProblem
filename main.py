import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 480, 480
CELL_SIZE = 60
BLACK = (150, 150, 150)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#get the queen image to plot it on screen
QUEEN_IMAGE = pygame.image.load('queen.png')
QUEEN_IMAGE = pygame.transform.scale(QUEEN_IMAGE, (CELL_SIZE, CELL_SIZE))

# Function to draw the chessboard
def draw_board(screen):
    screen.fill(WHITE)
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to draw the queens on the board
def draw_queens(screen, queens):
    for col, row in queens:
        screen.blit(QUEEN_IMAGE, (col * CELL_SIZE, row * CELL_SIZE))



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
        print(f'Generation: {generation}\n')
    return None  # Failed to find a solution within max generations

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('8 Queens Problem')
    # Load the icon image
    icon = pygame.image.load("icon.png")

    # Set the icon for the window
    pygame.display.set_icon(icon)
    queens = []
    running = True
    solved = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not solved:
                col = event.pos[0] // CELL_SIZE
                row = event.pos[1] // CELL_SIZE
                if 0 <= row < 8 and 0 <= col < 8:
                    queens.append((col, row))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not solved:
                initial_board = [queen[1] for queen in queens]
                solution = solve_queens(initial_board, population_size=100, mutation_rate=0.01, max_generations=1000000)
                if solution:
                    solved = True
                    queens = [(i, solution[i]) for i in range(8)]
                    print("Solution found:", queens)
                    pygame.image.save(screen, 'InitialQueensPosition.png')  # Save the board as a PNG image

                else:
                    print("Failed to find a solution.")

        draw_board(screen)
        draw_queens(screen, queens)
        if solved:
            draw_queens(screen, queens)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
