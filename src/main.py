import random
from tsp_problem import generate_cities
from tsp_problem import calculate_total_distance

NUM_CITIES = 30
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000

def main():

    print("Initializing...")
    cities = generate_cities(NUM_CITIES)

    population = []
    for _ in range(POPULATION_SIZE):
        route = list(range(NUM_CITIES))
        random.shuffle(route)
        population.append(route)

    best_overall_route = None
    best_overall_distance = float('inf')

    for generation in range(NUM_GENERATIONS):

        best_in_generation = None
        best_distance_in_generation = float('inf')    

        for individual in population:
            distance = calculate_total_distance(individual, cities)
            if distance < best_distance_in_generation:
                best_distance_in_generation = distance
                best_in_generation = individual

        if distance < best_overall_distance:
            best_overall_distance = best_distance_in_generation
            best_overall_route = best_in_generation
        
        # TODO: Add genetic algorithm operations (selection, crossover, mutation) here

        print(f"Generation {generation + 1} / {NUM_GENERATIONS}, Shortest distance = {best_distance_in_generation:.2f}")


        # printing finall results
        print("\n---End of evolution---")
        print(f"Shortest distance found: {best_overall_distance:.2f}")
        print(f"Best route: {best_overall_route}")


if __name__ == '__main__':
    main()