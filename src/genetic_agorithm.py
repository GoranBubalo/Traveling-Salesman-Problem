import random
from tsp_problem import calculate_total_distance

# Logic for tournament selection, finding the best route 
def tournament_selction(population,cities, k = 3):
    tournament = random.sample(population,k)

    best_individual = None
    best_distance = float('inf')

    for individual in tournament:
        current_distance = calculate_total_distance(individual, cities)

        if current_distance < best_distance:
            best_distance = current_distance
            best_individual = individual

    return best_individual

def pmx_crossover(parent1, parent2):
    size = len(parent1)
    child1, child2 = [-1] * size, [-1] * size

    start_pos = random.randint(0, size - 1)
    end_pos = random.randint(0, size - 1)

    if start_pos > end_pos:
        start_pos, end_pos = end_pos, start_pos
    
    child1[start_pos:end_pos] = parent1[start_pos:end_pos]
    child2[start_pos:end_pos] = parent2[start_pos:end_pos]

   
    def fill_gaps(child, parent1, parent2, start, end):
        mapping = {}
        for i in range(start, end):
            mapping[parent2[i]] = parent1[i]
        
        for i in range(size):
            if child[i] == -1:
                current_value = parent2[i]
                while current_value in mapping:
                    current_value = mapping[current_value]
                child[i] = current_value
    
    
    fill_gaps(child1, parent1, parent2, start_pos, end_pos)
    fill_gaps(child2, parent2, parent1, start_pos, end_pos)

    return child1, child2
    
# Inversion mutation function
def inversion_mutation(route):
    size = len(route)
    start = random.randint(0, size - 1)
    end = random.randint(0, size - 1)

    if start > end:
        start, end = end, start

    mutated_route = route[:] 
    mutated_route[start:end] = mutated_route[start:end][::-1]

    return mutated_route