import logging
import argparse
from codetiming import Timer
import pandas as pd
from utils.data_helper import extract_data
from src.algorithms.nearest_neighbor import nearest_neighbor_tsp

# Configuração do parser de argumentos
parser = argparse.ArgumentParser(description='Descrição do seu script.')
parser.add_argument('--algorithm', type=str, default="nn", help='Algoritmo a ser executado')
parser.add_argument('--instancia', type=str, default="sd", help='Instancia de teste')
parser.add_argument('--rounds', type=int, default=3, help='Número de repetições no teste')
args = parser.parse_args()

# Environment setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

# Dataframe_time_setup
# sd_df = pd.DataFrame(columns=['gr96', 'berlin52', 'pr76', 'ulysses22', 'att48'], index=range(5))
sd_df = {}
timers = {}
# Dataframe_solution_setup
solutions_sd_nn = {}

# Experiment Setup
data_s = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/small_data")
data_m = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/medium_data")
data_l = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/large_data")


def run_experiment_nn(alg: str = "nn"):
    solutions = {}
    logging.info("Small data:")
    t = Timer(name="class", logger=None, text="Time spent: {seconds:.4f}")
    alg_lst = {"nn": nearest_neighbor_tsp}

    for prob in data_s:
        t.start()
        solutions[prob["name"]] = alg_lst[alg](prob["node_coords"])
        t.stop()
        timers[prob["name"]] = t.last
        logging.info(prob["name"] + ":" + "Time spent: " + str(t.last))

    # sd_df.loc[0] = timestamp_lst  # insert timestamp list into dataframe
    solutions_sd_nn[0] = solutions  # insert solutions into dictionary

    # print(timers)



def main():
    run_experiment_nn(args.algorithm)

if __name__ == "__main__":
    main()
