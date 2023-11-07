import random
import math
from src.utils.helper import euclidean_distance, calculate_total_distance
# Dicionário de coordenadas das cidades (substitua pelas coordenadas reais)
city_coordinates = {
    0: (0, 0),
    1: (1, 2),
    2: (3, 4),
    3: (5, 6)
}

# Função para gerar uma solução vizinha (permutação das cidades)
def generate_neighbor(solution):
    neighbor = solution.copy()
    i, j = random.sample(range(len(solution)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

# Função para determinar se aceita a solução vizinha
def accept_neighbor(current_distance, neighbor_distance, temperature):
    if neighbor_distance < current_distance:
        return True
    probability = math.exp((current_distance - neighbor_distance) / temperature)
    return random.random() < probability

def simulated_annealing(initial_solution, max_iterations, initial_temperature, cooling_rate):
    current_solution = initial_solution
    current_distance = calculate_total_distance(current_solution)
    best_solution = current_solution
    best_distance = current_distance

    temperature = initial_temperature

    for _ in range(max_iterations):
        neighbor_solution = generate_neighbor(current_solution)
        neighbor_distance = calculate_total_distance(neighbor_solution)

        if accept_neighbor(current_distance, neighbor_distance, temperature):
            current_solution = neighbor_solution
            current_distance = neighbor_distance

        if current_distance < best_distance:
            best_solution = current_solution
            best_distance = current_distance

        # Reduzir a temperatura
        temperature *= cooling_rate

    return best_solution, best_distance

# Exemplo de uso:
num_cities = len(city_coordinates)
initial_solution = list(range(num_cities))  # Permutação inicial
max_iterations = 1000
initial_temperature = 1000.0
cooling_rate = 0.99

best_solution, best_distance = simulated_annealing(initial_solution, max_iterations, initial_temperature, cooling_rate)

print("Melhor solução encontrada:", best_solution)
print("Distância da melhor solução:", best_distance)
