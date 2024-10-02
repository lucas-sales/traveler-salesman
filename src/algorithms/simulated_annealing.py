import random
import math
from src.utils.math_helper import calculate_total_distance


# Função para gerar uma solução vizinha (permutação das cidades)
def generate_neighbor(solution):
    neighbor = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor


def generate_initial_solution(city_coordinates):
    cities = list(city_coordinates.keys())
    random.shuffle(cities)
    return cities


# Função para determinar se aceita a solução vizinha
def accept_neighbor(current_distance, neighbor_distance, temperature):
    if neighbor_distance < current_distance:
        return True
    probability = math.exp((current_distance - neighbor_distance) / temperature)
    return random.random() < probability


def simulated_annealing(city_coordinates,
                        max_iterations=1000,
                        initial_temperature=0.025,
                        cooling_rate=0.99):

    current_solution = generate_initial_solution(city_coordinates)
    current_distance = calculate_total_distance(city_coordinates, current_solution)
    best_solution = current_solution.copy()
    best_distance = current_distance

    temperature = initial_temperature

    for iteration in range(max_iterations):
        neighbor_solution = generate_neighbor(current_solution)
        neighbor_distance = calculate_total_distance(city_coordinates, neighbor_solution)

        if accept_neighbor(current_distance, neighbor_distance, temperature):
            current_solution = neighbor_solution
            current_distance = neighbor_distance

        if current_distance < best_distance:
            best_solution = current_solution.copy()
            best_distance = current_distance

        # Reduzir a temperatura
        temperature *= cooling_rate

        # Parar se a temperatura for muito baixa
        if temperature < 1e-10:
            break

    best_solution.append(best_solution[0])  # Retornar à cidade de origem para completar o ciclo
    return best_solution, str(best_distance)

# Exemplo de uso:
# Dicionário de coordenadas das cidades (substitua pelas coordenadas reais)
# city_coordinates = {
#     0: (0, 0),
#     1: (1, 2),
#     2: (3, 4),
#     3: (5, 6)
# }
# best_solution, best_distance = simulated_annealing(city_coordinates)
# print("Melhor solução encontrada:", best_solution)
# print("Distância da melhor solução:", best_distance)
