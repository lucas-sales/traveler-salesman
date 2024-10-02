import random
from collections import deque
from src.utils.math_helper import calculate_total_distance


def generate_neighbor(solution):
    neighbor = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor


def tabu_search(city_coordinates, max_iterations=1000, tabu_list_size=30):
    num_cities = len(city_coordinates)
    initial_solution = list(range(1, num_cities + 1))
    current_solution = initial_solution.copy()
    best_solution = current_solution.copy()
    tabu_list = deque(maxlen=tabu_list_size)
    iterations_without_improvement = 0
    max_iterations_without_improvement = max_iterations // 10

    best_distance = calculate_total_distance(city_coordinates, best_solution)

    for iteration in range(max_iterations):
        neighbor_solution = generate_neighbor(current_solution)

        # Evitar soluções tabu
        while neighbor_solution in tabu_list:
            neighbor_solution = generate_neighbor(current_solution)

        neighbor_distance = calculate_total_distance(city_coordinates, neighbor_solution)
        current_distance = calculate_total_distance(city_coordinates, current_solution)

        if neighbor_distance < current_distance:
            current_solution = neighbor_solution

            if neighbor_distance < best_distance:
                best_solution = neighbor_solution
                best_distance = neighbor_distance

            tabu_list.append(neighbor_solution)
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1

        if iterations_without_improvement >= max_iterations_without_improvement:
            current_solution = best_solution
            iterations_without_improvement = 0

    # Adicionar a rota de volta à cidade de origem
    best_solution.append(best_solution[0])
    custo = calculate_total_distance(city_coordinates, best_solution)
    return best_solution, str(custo)

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
