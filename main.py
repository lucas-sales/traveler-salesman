import logging
import argparse
from codetiming import Timer
from src.utils.data_helper import extract_data
from src.algorithms.nearest_neighbor import nearest_neighbor_tsp
from src.algorithms.ant_colony import ant_colony_optimization_tsp
from src.algorithms.tabu_search import tabu_search
from src.algorithms.genetic_algorithm import genetic_algorithm
from src.algorithms.simulated_annealing import simulated_annealing

# Argument parser configuration
parser = argparse.ArgumentParser(description='Descrição do seu script.')
parser.add_argument('--algorithm', type=str, default="nn", help='Algoritmo a ser executado')
parser.add_argument('--instance', type=str, default="sd", help='Instancia de teste')
parser.add_argument('--file', type=str, help='arquivo de teste')
args = parser.parse_args()

# Environment setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")


# Experiment Setup
data_s = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/small_data")
data_m = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/medium_data")
data_l = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/large_data")

# Algorithms available
algorithm_catalog = {"nn": nearest_neighbor_tsp,
                     "ts": tabu_search,
                     "ac": ant_colony_optimization_tsp,
                     "ga": genetic_algorithm,
                     "sa": simulated_annealing}


def run_algorithm(alg: str, inst: str, file: str) -> None:
    """
    :param alg: Algorithm to be executed
    :param inst: Instance of test
    :param file: File to be executed
    :return: Information about the experiment
    """

    logging.info(f'Executing algorithm {alg}, for the file {file}')
    if inst == "sd":
        current_instance = data_s
    elif inst == "md":
        current_instance = data_m
    elif inst == "ld":
        current_instance = data_l
    else:
        logging.error(f'Instance {inst} not founded!')
        exit()

    if current_instance:
        for f in current_instance:
            if f["name"] == file:
                t = Timer(name="class", logger=None, text="Time spent: {seconds:.4f}")
                t.start()
                solution = algorithm_catalog[alg](f["node_coords"])
                t.stop()
                logging.info(f["name"] + " - " + "Time spent: " + str(t.last))
                logging.info(f"Solution: {solution[0]}")
                logging.info("Distance: %.2f" % float(solution[1]))
                break


def main():
    run_algorithm(args.algorithm, args.instance, args.file)


if __name__ == "__main__":
    main()
