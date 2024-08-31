import time
from src.utils.data_helper import extract_data
from src.algorithms.genetic_algorithm import genetic_algorithm
from src.algorithms.nearest_neighbor import nearest_neighbor_tsp
from src.algorithms.tabu_search import tabu_search
from src.algorithms.simulated_annealing import simulated_annealing
from src.algorithms.ant_colony import ant_colony_optimization_tsp


# Função para adaptar os dados do formato do arquivo para o formato esperado pelos algoritmos
def prepare_data(data):
    return data["node_coords"]


# Extração dos dados
data_s = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/small_data")
data_m = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/medium_data")
data_l = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/large_data")

# Seleção dos datasets específicos
berlin52 = next(filter(lambda f: f["name"] == "berlin52", data_s), None)
eil101 = next(filter(lambda f: f["name"] == "eil101", data_m), None)
rat195 = next(filter(lambda f: f["name"] == "rat195", data_l), None)

# Preparação dos dados para serem usados pelos algoritmos
berlin52_coords = prepare_data(berlin52)
eil101_coords = prepare_data(eil101)
rat195_coords = prepare_data(rat195)


# Função para medir o tempo de execução
def measure_time(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    result = end_time - start_time

    print(f"Algorithm: {algorithm.__name__}")
    print(f"Tempo de execução: {result:.6f} segundos")
    print("-------------------------------------------------------")
    return result

if __name__ == "__main__":
    # small instances
    # result = measure_time(simulated_annealing, berlin52_coords)
    # result2 = measure_time(nearest_neighbor_tsp, berlin52_coords)
    # result3 = measure_time(tabu_search, berlin52_coords)
    # result4 = measure_time(ant_colony_optimization_tsp, berlin52_coords)
    # result5 = measure_time(genetic_algorithm, berlin52_coords)

    # medium instances
    # result = measure_time(simulated_annealing, eil101_coords)
    # result2 = measure_time(nearest_neighbor_tsp, eil101_coords)
    # result3 = measure_time(tabu_search, eil101_coords)
    # result4 = measure_time(ant_colony_optimization_tsp, eil101_coords)
    # result5 = measure_time(genetic_algorithm, eil101_coords)

    # large instances
    # result = measure_time(simulated_annealing, rat195_coords)
    # result2 = measure_time(nearest_neighbor_tsp, rat195_coords)
    result3 = measure_time(tabu_search, rat195_coords)
    result4 = measure_time(ant_colony_optimization_tsp, rat195_coords)
    result5 = measure_time(genetic_algorithm, rat195_coords)

    