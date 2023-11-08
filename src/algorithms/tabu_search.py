import random
from src.utils.helper import calculate_total_distance
# Dicionário de coordenadas das cidades (substitua pelas coordenadas reais)
city_coordinates = {
    1: (0, 0),
    2: (1, 2),
    3: (3, 4),
    4: (5, 6)
}


# Função para gerar uma solução vizinha (perturbação na solução atual)
def generate_neighbor(solution):
    neighbor = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

# Implementação da busca tabu
def tabu_search(initial_solution, max_iterations, tabu_list_size):
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

    return best_solution, calculate_total_distance(city_coordinates, best_solution)


# Exemplo de uso:
num_cities = len(city_coordinates)
initial_solution = list(range(1, num_cities + 1))  # Permutação inicial
max_iterations = 1000
tabu_list_size = num_cities // 2

best_solution, best_distance = tabu_search(initial_solution, max_iterations, tabu_list_size)

print("Melhor solução encontrada:", best_solution)
print("Distância da melhor solução:", best_distance)
