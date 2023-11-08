import random
from src.utils.helper import euclidean_distance


# Dicionário de coordenadas das cidades (substitua pelas coordenadas reais)
city_coordinates = {
    1: (0, 0),
    2: (1, 2),
    3: (3, 4),
    4: (5, 6)
}

# Parâmetros do ACO
num_ants = 10  # Número de formigas
alpha = 1.0    # Peso da trilha de feromônio
beta = 2.0     # Peso da heurística (distância entre cidades)
evaporation_rate = 0.5  # Taxa de evaporação do feromônio
pheromone_deposit = 1.0  # Quantidade de feromônio depositada por formiga


# Cálculo da matriz de distâncias
num_cities = len(city_coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        distance = euclidean_distance(city_coordinates[i + 1], city_coordinates[j + 1])
        distance_matrix[i][j] = distance
        distance_matrix[j][i] = distance

# Inicialização da matriz de feromônio
pheromone_matrix = [[1.0] * num_cities for _ in range(num_cities)]


# Função para calcular a probabilidade de transição
def calculate_transition_probabilities(ant, current_city, unvisited_cities, pheromone_matrix, distance_matrix, alpha, beta):
    probabilities = []
    total_probability = 0.0
    for city in unvisited_cities:
        pheromone = pheromone_matrix[current_city][city]
        distance = distance_matrix[current_city][city]
        probabilities.append(((current_city, city), (pheromone ** alpha) * ((1 / distance) ** beta)))
        total_probability += probabilities[-1][1]
    probabilities = [((a, b), p / total_probability) for (a, b), p in probabilities]
    return probabilities

# Loop principal do ACO
num_iterations = 100
for iteration in range(num_iterations):
    for ant in range(num_ants):
        unvisited_cities = list(range(num_cities))
        current_city = random.choice(unvisited_cities)
        unvisited_cities.remove(current_city)
        route = [current_city]

        while unvisited_cities:
            probabilities = calculate_transition_probabilities(ant, current_city, unvisited_cities, pheromone_matrix, distance_matrix, alpha, beta)
            next_city = random.choices(range(len(probabilities)), weights=[p for (_, p) in probabilities])[0]
            current_city = probabilities[next_city][0][1]
            route.append(current_city)
            unvisited_cities.remove(current_city)

        # Adicionar a rota de volta à cidade de origem
        route.append(route[0])

        # Cálculo do comprimento da rota
        route_length = sum(distance_matrix[route[i]][route[i + 1]] for i in range(num_cities))

        # Atualização do feromônio na rota da formiga
        for i in range(num_cities):
            city1 = route[i]
            city2 = route[i + 1]
            pheromone_matrix[city1][city2] += pheromone_deposit / route_length
            pheromone_matrix[city2][city1] += pheromone_deposit / route_length

    # Evaporação do feromônio
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone_matrix[i][j] *= (1 - evaporation_rate)

# Encontrar a melhor rota
best_route = route
best_distance = sum(distance_matrix[best_route[i]][best_route[i + 1]] for i in range(num_cities))

print("Melhor rota encontrada:", best_route)
print("Distância da melhor rota:", best_distance)
