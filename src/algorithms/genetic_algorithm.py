import random
from src.utils.math_helper import calculate_total_distance


# Função para gerar uma solução inicial
def generate_initial_solution(city_coordinates):
    """
    Gera uma solução inicial embaralhando as cidades.
    """
    cities = list(city_coordinates.keys())
    return random.sample(cities, len(cities))


# Função para realizar a seleção de pais com base na roleta
def select_parents(population, fitness):
    """
    Seleciona dois pais da população atual com base em suas aptidões usando roleta.
    """
    total_fitness = sum(fitness)
    probabilities = [fit / total_fitness for fit in fitness]
    parents = random.choices(population, probabilities, k=2)
    return parents


# Função para realizar crossover (ordem) entre dois pais
def crossover(parent1, parent2):
    """
    Realiza crossover do tipo ordem entre dois pais para gerar um filho.
    """
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start + 1, len(parent1))
    child = [-1] * len(parent1)
    for i in range(start, end):
        child[i] = parent1[i]
    p2_index = 0
    for i in range(len(child)):
        if child[i] == -1:
            while parent2[p2_index] in child:
                p2_index += 1
            child[i] = parent2[p2_index]
    return child


# Função de mutação: SWAP
def mutate_swap(solution):
    """
    Realiza mutação trocando dois genes aleatórios na solução (Swap).
    """
    index1, index2 = random.sample(range(len(solution)), 2)
    solution[index1], solution[index2] = solution[index2], solution[index1]


# Função de mutação: FLIP
def mutate_flip(solution):
    """
    Realiza mutação invertendo uma subsequência da solução (Flip).
    """
    index1, index2 = sorted(random.sample(range(len(solution)), 2))
    solution[index1:index2] = reversed(solution[index1:index2])


# Função de mutação: SLIDE
def mutate_slide(solution):
    """
    Realiza mutação deslocando uma subsequência da solução para uma nova posição (Slide).
    """
    index1, index2 = sorted(random.sample(range(len(solution)), 2))
    section = solution[index1:index2]
    solution = solution[:index1] + solution[index2:]
    insert_position = random.randint(0, len(solution) - 1)
    solution[insert_position:insert_position] = section
    return solution


# Função para realizar a mutação escolhendo entre Swap, Flip ou Slide
def mutate(solution):
    """
    Escolhe aleatoriamente uma entre as três mutações: Swap, Flip ou Slide.
    """
    mutation_type = random.choice([mutate_swap, mutate_flip, mutate_slide])
    if mutation_type == mutate_slide:
        return mutation_type(solution)
    else:
        mutation_type(solution)


# Implementação do Algoritmo Genético
def genetic_algorithm(city_coordinates,
                      num_generations=10000,
                      population_size=300,
                      crossover_probability=0.7,
                      mutation_probability=0.1,):
    """
    Implementa um Algoritmo Genético para resolver o Problema do Caixeiro Viajante.
    """

    # Inicializa a população
    population = [generate_initial_solution(city_coordinates) for _ in range(population_size)]

    for generation in range(num_generations):
        # Calcula a aptidão de cada solução
        fitness = [1 / calculate_total_distance(city_coordinates, solution) for solution in population]
        new_population = []

        # Gera nova população
        while len(new_population) < population_size:
            # Seleção de pais com base na roleta
            parents = select_parents(population, fitness)

            # Crossover com base na probabilidade
            if random.random() < crossover_probability:
                child1 = crossover(parents[0], parents[1])
                child2 = crossover(parents[1], parents[0])
            else:
                child1, child2 = parents[0][:], parents[1][:]

            # Mutação com base na probabilidade
            if random.random() < mutation_probability:
                mutate(child1)
            if random.random() < mutation_probability:
                mutate(child2)

            new_population.append(child1)
            new_population.append(child2)

        # Garantir que a nova população não exceda o tamanho da população original
        population = new_population[:population_size]

    # Seleciona a melhor solução
    best_solution = min(population, key=lambda solution: calculate_total_distance(city_coordinates, solution))
    best_solution.append(best_solution[0])  # Retornar à cidade de origem para completar o ciclo
    best_distance = calculate_total_distance(city_coordinates, best_solution)

    return best_solution, str(best_distance)

# Exemplo de uso:
# Dicionário de coordenadas das cidades (substitua pelas coordenadas reais)
# city_coordinate = {
#     1: [565.0, 575.0],
#     2: [25.0, 185.0],
#     3: [345.0, 750.0],
#     # Adicione mais coordenadas conforme necessário
# }

# best_solution, best_distance = genetic_algorithm(city_coordinate)

# print("Melhor solução encontrada:", best_solution)
# print("Distância da melhor solução:", best_distance)
