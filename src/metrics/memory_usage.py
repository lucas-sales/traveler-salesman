from src.algorithms.nearest_neighbor import nearest_neighbor_tsp
from src.algorithms.ant_colony import ant_colony_optimization_tsp
from src.algorithms.tabu_search import tabu_search
from src.algorithms.genetic_algorithm import genetic_algorithm
from src.algorithms.simulated_annealing import simulated_annealing
from src.utils.data_helper import extract_data

from memory_profiler import memory_usage
import time


data_s = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/small_data")
data_m = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/medium_data")
data_l = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/large_data")

berlin52 = next(filter(lambda f: f["name"] == "berlin52", data_s), None)
eil101 = next(filter(lambda f: f["name"] == "eil101", data_m), None)
rat195 = next(filter(lambda f: f["name"] == "rat195", data_l), None)


def measure_memory(function, *args, **kwargs):
    start_time = time.time()

    mem_usage, result = memory_usage((function, args, kwargs), interval=0.01, retval=True)

    end_time = time.time()

    print(f"Algorithm: {function.__name__}")
    print(f"Uso de memória: {max(mem_usage) - min(mem_usage)} MiB")
    print(f"Tempo de execução: {end_time - start_time} segundos")
    print("-------------------------------------------------------")

    return result


if __name__ == "__main__":

    # small instances
    # result = measure_memory(simulated_annealing, berlin52["node_coords"])
    result2 = measure_memory(nearest_neighbor_tsp, berlin52["node_coords"])
    # result3 = measure_memory(tabu_search, berlin52["node_coords"])
    # result4 = measure_memory(ant_colony_optimization_tsp, berlin52["node_coords"])
    # result5 = measure_memory(genetic_algorithm, berlin52["node_coords"])


    # medium instances
    # result = measure_memory(simulated_annealing, eil101["node_coords"])
    # result2 = measure_memory(nearest_neighbor_tsp, eil101["node_coords"])
    # result3 = measure_memory(tabu_search, eil101["node_coords"])
    # result4 = measure_memory(ant_colony_optimization_tsp, eil101["node_coords"])
    # result5 = measure_memory(genetic_algorithm, eil101["node_coords"])

    # large instances
    # result = measure_memory(simulated_annealing, rat195["node_coords"])
    # result2 = measure_memory(nearest_neighbor_tsp, rat195["node_coords"])
    # result3 = measure_memory(tabu_search, rat195["node_coords"])
    # result4 = measure_memory(ant_colony_optimization_tsp, rat195["node_coords"])
    # result5 = measure_memory(genetic_algorithm, rat195["node_coords"])
