import random 
import math

# Function for generating cities
def generate_cities(num_cities, x_range=(0,100), y_range=(0,100)):
    cities = []
    for _ in range(num_cities):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        cities.append((x,y))
    return cities

# Fitness function for finding the best route (shortes route)
def calculate_total_distance(route, cities):
    total_distance = 0
    num_cities = len(route)

    # Distance between cities
    for i in range(num_cities - 1):
        city1_index = route[i]
        city2_index = route[i + 1]
        city1 = cities[city1_index]
        city2 = cities[city2_index]
        total_distance += euclidian_distance(city1, city2) 

    # From last city to the first city 
    last_city_index = route[num_cities - 1]
    first_city_index = route[0]
    last_city = cities[last_city_index]
    first_city = cities[first_city_index]
    total_distance += euclidian_distance(last_city,first_city)

    return total_distance
 
# function for calculating euclidian distance
def euclidian_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# testing code 
if __name__ == '__main__':
    cities = generate_cities(30)
    print("Generating 30 cities, first 5 examples: ")
    print(cities[:5])

    distance = euclidian_distance(cities[0], cities[1])
    print("\nDistance between first and second city is ", distance)

    initial_route = list(range(30))
    random.shuffle(initial_route)

    total_distance = calculate_total_distance(initial_route, cities)
    print("All together the distance of random route is :", total_distance)