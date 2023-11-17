import logging
from codetiming import Timer
import pandas as pd
from utils.data_helper import extract_data
from src.algorithms.nearest_neighbor import nearest_neighbor_tsp

# Environment setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

t = Timer(name="class", text="Time spent: {seconds:.4f}")

# Dataframe_time_setup
sd_nn_df = pd.DataFrame(columns=['gr96', 'berlin52', 'pr76', 'ulysses22', 'att48'], index=range(5))

# Dataframe_solution_setup
solutions_sd_nn = {}

# Experiment Setup
data_s = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/small_data")
data_m = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/medium_data")
data_l = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/large_data")
print(data_s)


def run_experiment_nn(itr: int):
    timestamp_lst = []
    solutions = {}
    logging.info("Small data:")
    for prob in data_s:
        t.start()
        solutions[prob["name"]] = nearest_neighbor_tsp(prob["node_coords"])
        t.stop()
        timestamp_lst.append(t.last)
        logging.info("Time spent: " + str(t.last))
        # images(prob["node_coords"], solutions)

    sd_nn_df.loc[itr] = timestamp_lst  # insert timestamp list into dataframe
    solutions_sd_nn[itr] = solutions  # insert solutions into dictionary

    print(sd_nn_df)
    print(solutions_sd_nn)

    # for prob in data_m:
    #     print(prob["name"] + ":")
    #     print(nearest_neighbor_tsp(prob["node_coords"]))
    #
    # for prob in data_l:
    #     print(prob["name"] + ":")
    #     print(nearest_neighbor_tsp(prob["node_coords"]))


def run_experiment_sa(itr: str):
    return True


def run_experiment_ga(itr: str):
    return True


def run_experiment_aco(itr: str):
    return True


def run_experiment_ts(itr: str):
    return True


def run_experiment_tpo(itr: str):
    return True


algorithms_list = [run_experiment_nn, run_experiment_sa]


def main():
    for alg in algorithms_list:
        # Experiment Execution
        logging.info("Starting experiment with NN algorithm...")

        for itr in range(5):
            alg(itr)


main()
