import os
import pandas as pd
import tsplib95
import logging


def extract_data(path: str):
    problem_list = []
    arr = os.listdir(path)
    for file in arr:
        problem = tsplib95.load(path + "/" + file)
        problem_list.append(problem.as_dict())
    return problem_list


def get_dataframes_by_instance(instance: str):
    data_s = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/small_data")
    data_m = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/medium_data")
    data_l = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/large_data")

    if instance == "sd":
        return data_s
    elif instance == "md":
        return data_m
    elif instance == "ld":
        return data_l
    else:
        logging.error(f'Instance {instance} not founded!')
        return None


def get_results_dataframes():
    df_p = pd.read_csv('/Users/lucassales/Dev/TCC/traveler-salesman/tables/Resultados_inst_pequena.csv')
    df_m = pd.read_csv('/Users/lucassales/Dev/TCC/traveler-salesman/tables/Resultados_inst_media.csv')
    df_g = pd.read_csv('/Users/lucassales/Dev/TCC/traveler-salesman/tables/Resultados_inst_grande.csv')
    return df_p, df_m, df_g


def calculate_mean_time_by_algorithm_and_file(df):
    """
    Calcula a média dos tempos para cada algoritmo e cada arquivo (File name).
    """
    # Agrupar por algoritmo e nome do arquivo e calcular a média do tempo gasto
    mean_times = df.groupby(['algorithm', 'File name'])['Time spent'].mean().unstack()
    return mean_times