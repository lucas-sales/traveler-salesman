import random
from src.utils.math_helper import euclidean_distance, calculate_total_distance


# Função para encontrar o próximo vizinho mais próximo a partir de uma cidade
def find_nearest_neighbor(city, unvisited_cities):
    """
    :param city:
    :param unvisited_cities:
    :return:
    """
    nearest_distance = float('inf')
    nearest_city = None

    for neighbor, coords in unvisited_cities.items():
        distance = euclidean_distance(city, coords)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_city = neighbor

    return nearest_city, nearest_distance


# Algoritmo do Vizinho Mais Próximo para encontrar o caminho
def nearest_neighbor_tsp(coordinates, num_iterations=1000):
    best_path = None
    best_custo = float('inf')

    for _ in range(num_iterations):
        # Escolher uma cidade inicial aleatória
        initial_city = random.choice(list(coordinates.keys()))

        path = [initial_city]
        unvisited_cities = coordinates.copy()
        del unvisited_cities[initial_city]

        while unvisited_cities:
            current_city = path[-1]
            nearest_city, _ = find_nearest_neighbor(coordinates[current_city], unvisited_cities)
            path.append(nearest_city)
            del unvisited_cities[nearest_city]

        path.append(path[0])  # Retornar à cidade de origem para completar o ciclo
        custo = calculate_total_distance(coordinates, path)

        if custo < best_custo:
            best_path = path
            best_custo = custo

    return best_path, str(best_custo)
