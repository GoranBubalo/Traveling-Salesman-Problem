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

    ## TODO: Finish function 


 
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