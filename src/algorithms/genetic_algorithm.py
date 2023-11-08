import random



# Função para calcular a distância euclidiana entre duas cidades
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Função para calcular o custo de uma solução (distância total percorrida no TSP)
def calculate_total_distance(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += euclidean_distance(city_coordinates[solution[i]], city_coordinates[solution[i+1]])
    total_distance += euclidean_distance(city_coordinates[solution[-1]], city_coordinates[solution[0]])  # Retornar à cidade de origem
    return total_distance

# Função para gerar uma solução inicial
def generate_initial_solution():
    cities = list(city_coordinates.keys())
    random.shuffle(cities)
    return cities

# Função para realizar a seleção de pais com base na roleta
def select_parents(population, fitness):
    total_fitness = sum(fitness)
    probabilities = [fit / total_fitness for fit in fitness]
    parents = random.choices(population, probabilities, k=2)
    return parents

# Função para realizar crossover (ordem) entre dois pais
def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start + 1, len(parent1))
    child = [-1] * len(parent1)
    for i in range(start, end):
        child[i] = parent1[i]
    for i in range(len(parent2)):
        if parent2[i] not in child:
            for j in range(len(child)):
                if child[j] == -1:
                    child[j] = parent2[i]
                    break
    return child

# Função para realizar mutação (inversão) em uma solução
def mutate(solution):
    index1, index2 = random.sample(range(len(solution)), 2)
    solution[index1], solution[index2] = solution[index2], solution[index1]

# Implementação do Algoritmo Genético
def genetic_algorithm(num_generations, population_size, crossover_probability, mutation_probability):
    population = [generate_initial_solution() for _ in range(population_size)]

    for generation in range(num_generations):
        fitness = [1 / calculate_total_distance(solution) for solution in population]
        new_population = []

        while len(new_population) < population_size:
            parents = select_parents(population, fitness)

            if random.random() < crossover_probability:
                child1 = crossover(parents[0], parents[1])
                child2 = crossover(parents[1], parents[0])
            else:
                child1, child2 = parents[0][:], parents[1][:]

            if random.random() < mutation_probability:
                mutate(child1)
            if random.random() < mutation_probability:
                mutate(child2)

            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    best_solution = min(population, key=lambda solution: calculate_total_distance(solution))
    best_distance = calculate_total_distance(best_solution)

    return best_solution, best_distance


# Exemplo de uso:

# Dicionário de coordenadas das cidades (substitua pelas coordenadas reais)
city_coordinates = {
    1: (0, 0),
    2: (1, 2),
    3: (3, 4),
    4: (5, 6)
}
num_generations = 100
population_size = 100
crossover_probability = 0.7
mutation_probability = 0.1

best_solution, best_distance = genetic_algorithm(num_generations, population_size, crossover_probability, mutation_probability)

print("Melhor solução encontrada:", best_solution)
print("Distância da melhor solução:", best_distance)
