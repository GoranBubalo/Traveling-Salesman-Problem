import random
from src.tsp_problem import calculate_total_distance

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