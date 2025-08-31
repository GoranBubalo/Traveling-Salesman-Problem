import random
from genetic_agorithm import tournament_selction, pmx_crossover, inversion_mutation
from tsp_problem import generate_cities
from tsp_problem import calculate_total_distance
import matplotlib.pyplot as plt
import matplotlib


NUM_CITIES = 30
POPULATION_SIZE = 20
NUM_GENERATIONS = 1000


def plot_route(cities, route, generation, distance):
    x = [cities[i][0] for i in route] + [cities[route[0]][0]]
    y = [cities[i][1] for i in route] + [cities[route[0]][1]]
    plt.clf()
    plt.plot(x, y, marker='o')
    plt.title(f'Generacija {generation} | Najkraći put: {distance:.2f}')
    plt.pause(0.01)

def main():

    print("Initializing...")
    cities = generate_cities(NUM_CITIES)
    plt.ion()

    population = []
    for _ in range(POPULATION_SIZE):
        route = list(range(NUM_CITIES))
        random.shuffle(route)
        population.append(route)

    best_overall_route = None
    best_overall_distance = float('inf')

    for generation in range(NUM_GENERATIONS):

        best_in_generation = min(population, key=lambda x: calculate_total_distance(x, cities))
        current_best_distance = calculate_total_distance(best_in_generation, cities)

        if generation % 10 == 0 or generation == NUM_GENERATIONS - 1:
            plot_route(cities, best_in_generation, generation + 1, current_best_distance)

        if current_best_distance < best_overall_distance:
            best_overall_distance = current_best_distance
            best_overall_route = best_in_generation
 
        new_population = [best_in_generation]

        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selction(population, cities)
            parent2 = tournament_selction(population, cities)

            # Checking if valid  , if not valid ignore and move to next parent
            while parent1 == parent2:
                parent2 = tournament_selction(population, cities)
            child1, child2 = pmx_crossover(parent1, parent2)

            if len(set(child1)) == NUM_CITIES and len(set(child2)) == NUM_CITIES:
                new_population.append(child1)
                if len(new_population) < POPULATION_SIZE:
                    new_population.append(child2)
            
           
        new_population = new_population[:POPULATION_SIZE]

        mutation_rate = 0.05
        for i in range(1, len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = inversion_mutation(new_population[i])
        
        population = new_population

        print(f"Generation {generation + 1}/{NUM_GENERATIONS}: Shortest route  = {current_best_distance:.2f}")

    # printing finall results
    print("\n---End of evolution---")
    print(f"Shortest distance found: {best_overall_distance:.2f}")
    print(f"Best route: {best_overall_route}")

    plt.ioff()
    plt.show()
    matplotlib.use('TkAgg')


if __name__ == '__main__':
    main()