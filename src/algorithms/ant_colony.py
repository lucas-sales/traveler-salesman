import random
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from src.utils.math_helper import euclidean_distance


def calculate_transition_probabilities(current_city, unvisited_cities, pheromone_matrix, distance_matrix, alpha, beta):
    """
    Calcula as probabilidades de transição para a formiga dada a cidade atual.
    """
    pheromones = pheromone_matrix[current_city, unvisited_cities]
    distances = distance_matrix[current_city, unvisited_cities]
    attractiveness = (pheromones ** alpha) * ((1.0 / distances) ** beta)

    total_attractiveness = np.sum(attractiveness)

    if total_attractiveness == 0:
        return None

    probabilities = attractiveness / total_attractiveness
    return unvisited_cities, probabilities


def build_route(ant, num_cities, pheromone_matrix, distance_matrix, alpha, beta):
    """
    Função que cada formiga executa para construir uma rota.
    """
    unvisited_cities = list(range(num_cities))
    current_city = random.choice(unvisited_cities)
    route = [current_city]
    unvisited_cities.remove(current_city)

    while unvisited_cities:
        probabilities = calculate_transition_probabilities(
            current_city, unvisited_cities, pheromone_matrix, distance_matrix, alpha, beta
        )
        if not probabilities:
            break
        unvisited_cities, probabilities = probabilities
        next_city_index = random.choices(range(len(probabilities)), weights=probabilities)[0]
        next_city = unvisited_cities[next_city_index]
        current_city = next_city
        route.append(current_city)
        unvisited_cities.remove(current_city)

    # Adicionar a rota de volta à cidade de origem se a rota estiver completa
    if len(route) == num_cities:
        route.append(route[0])

    # Cálculo do comprimento da rota usando a matriz de distâncias
    if len(route) == num_cities + 1:
        route_length = sum(distance_matrix[route[i]][route[i + 1]] for i in range(num_cities))
        return route, route_length
    return None


def ant_colony_optimization_tsp(city_dict,
                                num_iterations=1000,
                                num_ants=20,
                                alpha=1.0,
                                beta=1.0,
                                evaporation_rate=0.95,
                                pheromone_deposit=1.0):
    city_coordinates = [city_dict[i] for i in sorted(city_dict.keys())]

    num_cities = len(city_coordinates)
    distance_matrix = np.zeros((num_cities, num_cities))

    # Preenchendo a matriz de distâncias
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = euclidean_distance(city_coordinates[i], city_coordinates[j])
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    pheromone_matrix = np.ones((num_cities, num_cities))

    best_route = None
    best_distance = float('inf')

    for iteration in range(num_iterations):
        all_routes = []

        # Paralelizar a construção das rotas usando ProcessPoolExecutor
        with ThreadPoolExecutor(max_workers=6) as executor:
            futures = [executor.submit(build_route, ant, num_cities, pheromone_matrix, distance_matrix, alpha, beta)
                       for ant in range(num_ants)]

            for future in futures:
                result = future.result()
                if result:
                    all_routes.append(result)

        # Atualização da matriz de feromônios com evaporação e depósito
        for route, route_length in all_routes:
            for i in range(num_cities):
                city1 = route[i]
                city2 = route[i + 1]
                # Aplicar evaporação na aresta específica
                pheromone_matrix[city1][city2] *= (1 - evaporation_rate)
                pheromone_matrix[city2][city1] *= (1 - evaporation_rate)
                # Atualizar com depósito de feromônio
                pheromone_matrix[city1][city2] += pheromone_deposit / route_length
                pheromone_matrix[city2][city1] += pheromone_deposit / route_length

        # Atualização da melhor solução encontrada
        for route, route_length in all_routes:
            if route_length < best_distance:
                best_route = route
                best_distance = route_length

    # Verificar a validade da melhor rota
    if best_route is not None and len(set(best_route)) == num_cities and best_route[0] == best_route[-1]:
        print("Solução válida encontrada.")
    else:
        print("A solução encontrada não é válida.")

    return best_route, str(best_distance)
