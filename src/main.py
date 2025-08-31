import random
from genetic_agorithm import tournament_selction, pmx_crossover, inversion_mutation
from tsp_problem import generate_cities
from tsp_problem import calculate_total_distance

NUM_CITIES = 30
POPULATION_SIZE = 20
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

        best_in_generation = min(population, key=lambda x: calculate_total_distance(x, cities))
        current_best_distance = calculate_total_distance(best_in_generation, cities)

        if current_best_distance < best_overall_distance:
            best_overall_distance = current_best_distance
            best_overall_route = best_in_generation
 
        new_population = [best_in_generation]

        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selction(population, cities)
            parent2 = tournament_selction(population, cities)

            # Checking if valid  (Temporaly fix), if not valid ignore and move to next parent
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

        print(f"Generacija {generation + 1}/{NUM_GENERATIONS}: Najkraći put = {current_best_distance:.2f}")

    # printing finall results
    print("\n---End of evolution---")
    print(f"Shortest distance found: {best_overall_distance:.2f}")
    print(f"Best route: {best_overall_route}")


if __name__ == '__main__':
    main()