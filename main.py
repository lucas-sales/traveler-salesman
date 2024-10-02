import logging
import argparse
from codetiming import Timer
from memory_profiler import memory_usage
import pandas as pd
from src.algorithms.nearest_neighbor import nearest_neighbor_tsp
from src.algorithms.ant_colony import ant_colony_optimization_tsp
from src.algorithms.tabu_search import tabu_search
from src.algorithms.genetic_algorithm import genetic_algorithm
from src.algorithms.simulated_annealing import simulated_annealing
import src.utils.data_helper as dh

# Argument parser configuration
parser = argparse.ArgumentParser(description='Descrição do seu script.')
parser.add_argument('--instance', type=str, default="sd", help='Instancia de teste')
args = parser.parse_args()

# Environment setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")


def run_algorithm(inst: str):
    """
    :param inst: Instance of test
    :return: Information about the experiment
    """

    results = []

    # Algorithms available
    algorithm_catalog = {"nn": nearest_neighbor_tsp,
                         "ts": tabu_search,
                         "ac": ant_colony_optimization_tsp,
                         "ga": genetic_algorithm,
                         "sa": simulated_annealing}

    algorithm_seq = ["nn", "ts", "ga", "sa", "ac"]
    current_instance = dh.get_dataframes_by_instance(inst)

    if current_instance:
        for f in current_instance:
            for alg in algorithm_seq:
                logging.info(f'Executing algorithm {alg}, for the file {f["name"]}')
                t = Timer(name="class", logger=None, text="Time spent: {seconds:.4f}")
                t.start()
                mem_usage, solution = memory_usage(
                    (algorithm_catalog[alg], (f["node_coords"],)),
                    interval=0.01, retval=True)
                t.stop()

                logging.info(f["name"] + " - " + "Time spent: " + str(t.last))
                logging.info("-------------------------------------------------------")

                results.append({
                    'File name': f["name"],
                    'algorithm': alg,
                    'Time spent': round(t.last, 2),
                    'Memory used': round(max(mem_usage) - min(mem_usage), 2),
                    'Total distance': round(float(solution[1]), 2)
                })
        return results
    else:
        logging.error(f'Instance {inst} not founded!')
        return None


def main():
    results = run_algorithm(args.instance)
    df = pd.DataFrame(results)
    df.to_csv('experiment_results.csv', index=False)


if __name__ == "__main__":
    main()
