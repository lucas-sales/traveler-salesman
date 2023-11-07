import numpy as np


def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Função para calcular o custo de uma solução (distância total percorrida no TSP)
def calculate_total_distance(city_coordinates, solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        city1 = city_coordinates[solution[i]]
        city2 = city_coordinates[solution[i + 1]]
        total_distance += euclidean_distance(city1, city2)
    total_distance += euclidean_distance(city_coordinates[solution[-1]],
                                         city_coordinates[solution[0]])  # Retornar à cidade de origem
    return total_distance
