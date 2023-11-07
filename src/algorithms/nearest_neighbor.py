from src.utils.helper import euclidean_distance, calculate_total_distance
from src.utils.data_helper import extract_data


# Função para encontrar o próximo vizinho mais próximo a partir de uma cidade
def find_nearest_neighbor(city, unvisited_cities):
    nearest_distance = float('inf')
    nearest_city = None

    for neighbor, coords in unvisited_cities.items():
        distance = euclidean_distance(city, coords)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_city = neighbor

    return nearest_city, nearest_distance


# Algoritmo do Vizinho Mais Próximo para encontrar o caminho
def nearest_neighbor_tsp(coordinates):
    num_cities = len(coordinates)
    path = [1]  # Começamos na cidade 1 (pode ser qualquer cidade inicial)
    unvisited_cities = coordinates.copy()  # Todas as cidades, exceto a cidade de origem

    del unvisited_cities[1]  # Remove a cidade de origem

    while unvisited_cities:
        current_city = path[-1]
        nearest_city, _ = find_nearest_neighbor(coordinates[current_city], unvisited_cities)
        path.append(nearest_city)
        del unvisited_cities[nearest_city]

    path.append(path[0])  # Retornar à cidade de origem para completar o ciclo
    custo = calculate_total_distance(coordinates, path)
    print("Custo: " + str(custo))
    return path
