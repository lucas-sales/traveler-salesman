import random
from src.utils.helper import calculate_total_distance


# Função para gerar uma solução inicial
def generate_initial_solution(city_coordinates):
    """
    :param city_coordinates:
    :return:
    """
    cities = list(city_coordinates.keys())
    random.shuffle(cities)
    return cities


# Função para realizar a seleção de pais com base na roleta
def select_parents(population, fitness):
    """
    :param population:
    :param fitness:
    :return:
    """
    total_fitness = sum(fitness)
    probabilities = [fit / total_fitness for fit in fitness]
    parents = random.choices(population, probabilities, k=2)
    return parents


# Função para realizar crossover (ordem) entre dois pais
def crossover(parent1, parent2):
    """
    :param parent1:
    :param parent2:
    :return:
    """
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
    """
    :param solution:
    :return:
    """
    index1, index2 = random.sample(range(len(solution)), 2)
    solution[index1], solution[index2] = solution[index2], solution[index1]


# Implementação do Algoritmo Genético
def genetic_algorithm(city_coordinates):
    """
    :param city_coordinates:
    :return:
    """
    num_generations = 10000
    population_size = 300
    crossover_probability = 0.7
    mutation_probability = 0.1

    population = [generate_initial_solution(city_coordinates) for _ in range(population_size)]

    for generation in range(num_generations):
        fitness = [1 / calculate_total_distance(city_coordinates, solution) for solution in population]
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

    best_solution = min(population, key=lambda solution: calculate_total_distance(city_coordinates, solution))
    best_solution.append(best_solution[0])  # Retornar à cidade de origem para completar o ciclo
    best_distance = calculate_total_distance(city_coordinates, best_solution)
    return best_solution, str(best_distance)


# Exemplo de uso:

# Dicionário de coordenadas das cidades (substitua pelas coordenadas reais)
# city_coordinate ={
#     2: (1, 2),
#     3: (3, 4),
#     4: (5, 6)
# }


# best_solution, best_distance = genetic_algorithm(city_coordinate)

# print("Melhor solução encontrada:", best_solution)
# print("Distância da melhor solução:", best_distance)
