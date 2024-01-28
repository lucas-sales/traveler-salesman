import random
from src.utils.helper import calculate_total_distance


# Função para gerar uma solução vizinha (perturbação na solução atual)
def generate_neighbor(solution):
    """
    :param solution:
    :return:
    """
    neighbor = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor


# Implementação da busca tabu
def tabu_search(city_coordinates):
    """

    :param city_coordinates:
    :return:
    """
    num_cities = len(city_coordinates)
    initial_solution = list(range(1, num_cities + 1))  # Permutação inicial
    max_iterations = 1000
    tabu_list_size = num_cities // 2
    current_solution = initial_solution
    best_solution = current_solution
    tabu_list = []
    iterations_without_improvement = 0

    for iteration in range(max_iterations):
        neighbor_solution = generate_neighbor(current_solution)

        # Evitar soluções na lista tabu
        while neighbor_solution in tabu_list:
            neighbor_solution = generate_neighbor(current_solution)

        neighbor_distance = calculate_total_distance(city_coordinates, neighbor_solution)
        current_distance = calculate_total_distance(city_coordinates, current_solution)

        if neighbor_distance < current_distance:
            current_solution = neighbor_solution

            # Atualização da melhor solução encontrada
            if neighbor_distance < calculate_total_distance(city_coordinates, best_solution):
                best_solution = neighbor_solution

            # Adicionar a solução atual à lista tabu
            tabu_list.append(current_solution)
            if len(tabu_list) > tabu_list_size:
                tabu_list.pop(0)

            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1

        if iterations_without_improvement >= max_iterations // 10:
            # Reiniciar a busca para escapar de mínimos locais
            current_solution = best_solution

    best_solution.append(best_solution[0])  # Retornar à cidade de origem para completar o ciclo
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
