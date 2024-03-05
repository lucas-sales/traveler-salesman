import random
from collections import deque
from src.utils.helper import calculate_total_distance


def generate_neighbor(solution):
    neighbor = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor


def tabu_search(city_coordinates):
    num_cities = len(city_coordinates)
    initial_solution = list(range(1, num_cities + 1))
    max_iterations = 10000
    tabu_list_size = num_cities // 2
    current_solution = initial_solution
    best_solution = current_solution
    tabu_list = deque(maxlen=tabu_list_size)
    iterations_without_improvement = 1000

    for iteration in range(max_iterations):
        neighbor_solution = generate_neighbor(current_solution)

        while neighbor_solution in tabu_list:
            neighbor_solution = generate_neighbor(current_solution)

        neighbor_distance = calculate_total_distance(city_coordinates, neighbor_solution)
        current_distance = calculate_total_distance(city_coordinates, current_solution)

        if neighbor_distance < current_distance:
            current_solution = neighbor_solution

            if neighbor_distance < calculate_total_distance(city_coordinates, best_solution):
                best_solution = neighbor_solution

            tabu_list.append(neighbor_solution)
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1

        if iterations_without_improvement >= max_iterations // 10:
            current_solution = best_solution

    best_solution.append(best_solution[0])
    custo = calculate_total_distance(city_coordinates, best_solution)
    return best_solution, str(custo)


# Exemplo de uso:

# Dicionário de coordenadas das cidades (substitua pelas coordenadas reais)
# city_coordinates = {
#     1: (0, 0),
#     2: (1, 2),
#     3: (3, 4),
#     4: (5, 6)
# }
# best_solution, best_distance = tabu_search(city_coordinates)
#
# print("Melhor solução encontrada:", best_solution)
# print("Distância da melhor solução:", best_distance)
