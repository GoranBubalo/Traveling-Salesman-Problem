import random
from tsp_problem import generate_cities

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
    
                

if __name__ == '__main__':
    main()