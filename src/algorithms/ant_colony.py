import random
import numpy as np
from src.utils.helper import euclidean_distance, calculate_total_distance

def calculate_transition_probabilities(ant, current_city, unvisited_cities, pheromone_matrix, distance_matrix, alpha, beta):
    """
    Calcula as probabilidades de transição para a formiga dada a cidade atual.
    """
    probabilities = []
    total_probability = 0.0
    for city in unvisited_cities:
        pheromone = pheromone_matrix[current_city][city]
        distance = distance_matrix[current_city][city]
        probabilities.append(((current_city, city), (pheromone ** alpha) * ((1 / distance) ** beta)))
        total_probability += probabilities[-1][1]
    probabilities = [((a, b), p / total_probability) for (a, b), p in probabilities]
    return probabilities

def ant_colony_optimization_tsp(city_coordinates, num_ants=300, alpha=1.0, beta=1.0, evaporation_rate=0.95, pheromone_deposit=1.0, num_iterations=100):
# def ant_colony_optimization_tsp(city_coordinates, num_ants=48, alpha=1.0, beta=1.0, evaporation_rate=0.95, pheromone_deposit=1.0, num_iterations=48):
    """
    Implementação do Algoritmo de Colônia de Formigas para o Problema do Caixeiro Viajante (TSP).
    """
    num_cities = len(city_coordinates)
    distance_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = euclidean_distance(city_coordinates[i + 1], city_coordinates[j + 1])
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    pheromone_matrix = np.ones((num_cities, num_cities))

    best_route = None
    best_distance = float('inf')

    for iteration in range(num_iterations):
        for ant in range(num_ants):
            unvisited_cities = list(range(num_cities))
            current_city = random.choice(unvisited_cities)
            unvisited_cities.remove(current_city)
            route = [current_city]

            while unvisited_cities:
                probabilities = calculate_transition_probabilities(
                    ant, current_city, unvisited_cities, pheromone_matrix, distance_matrix, alpha, beta
                )
                next_city = random.choices(range(len(probabilities)), weights=[p for (_, p) in probabilities])[0]
                current_city = probabilities[next_city][0][1]
                route.append(current_city)
                unvisited_cities.remove(current_city)

            # Adicionar a rota de volta à cidade de origem
            route.append(route[0])

            # Cálculo do comprimento da rota
            route_length = sum(distance_matrix[route[i]][route[i + 1]] for i in range(num_cities))

            # Atualização do feromônio na rota da formiga
            for i in range(num_cities):
                city1 = route[i]
                city2 = route[i + 1]
                pheromone_matrix[city1][city2] += pheromone_deposit / route_length
                pheromone_matrix[city2][city1] += pheromone_deposit / route_length

            # Atualização da melhor solução encontrada
            if route_length < best_distance:
                best_route = route
                best_distance = route_length

        # Evaporação do feromônio
        pheromone_matrix *= (1 - evaporation_rate)

    # Verificar a validade da melhor rota
    if len(set(best_route)) == len(best_route) - 1 == num_cities:
        print("Solução válida encontrada.")
    else:
        print("A solução encontrada não é válida.")

    return best_route, str(best_distance)
