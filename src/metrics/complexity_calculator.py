import pandas as pd
from scipy.optimize import curve_fit
import numpy as np


# Função polinomial para ajuste de curva (n^b)
def poly_func(n, a, b):
    return a * n ** b


def calculate_mean_time_by_algorithm_and_file(df):
    """
    Calcula a média dos tempos para cada algoritmo e cada arquivo (File name).
    """
    # Agrupar por algoritmo e nome do arquivo e calcular a média do tempo gasto
    mean_times = df.groupby(['algorithm', 'File name'])['Time spent'].mean().unstack()
    return mean_times


# Preencher a estrutura 'time_usage' com as médias
def add_means_to_time_usage(mean_times, time_usage):
    for algorithm in time_usage.keys():
        if algorithm in mean_times.index:
            time_usage[algorithm].extend(mean_times.loc[algorithm].values)


# Função para obter a complexidade de cada algoritmo
def get_complexity(time_usage):
    complexities = {}
    for algorithm, times in time_usage.items():
        times = np.array(times)
        if len(times) == len(n_values):  # Verificar se o comprimento é compatível
            popt, _ = curve_fit(poly_func, n_values, times)
            a, b = popt
            complexities[algorithm] = (a, b)  # a é o coeficiente, b é o expoente que define a complexidade
        else:
            print(f"Algoritmo {algorithm} tem um número incompatível de amostras")
    return complexities


# Carregar o DataFrame do CSV
df = pd.read_csv('/Users/lucassales/Dev/TCC/traveler-salesman/tables/Resultados_inst_grande.csv')

# Definir as colunas para cada uma das três execuções
columns_part_1 = ['numero do experimento', 'File name', 'algorithm', 'Time spent', 'Memory used', 'Total distance']
columns_part_2 = ['numero do experimento.1', 'File name.1', 'algorithm.1', 'Time spent.1', 'Memory used.1',
                  'Total distance.1']
columns_part_3 = ['numero do experimento.2', 'File name.2', 'algorithm.2', 'Time spent.2', 'Memory used.2',
                  'Total distance.2']

# Criar três DataFrames, um para cada execução
df_part_1 = df[columns_part_1]
df_part_2 = df[columns_part_2]
df_part_3 = df[columns_part_3]

# Renomear as colunas para um formato mais simples (sem sufixos .1, .2, etc.)
df_part_1.columns = ['numero do experimento', 'File name', 'algorithm', 'Time spent', 'Memory used', 'Total distance']
df_part_2.columns = ['numero do experimento', 'File name', 'algorithm', 'Time spent', 'Memory used', 'Total distance']
df_part_3.columns = ['numero do experimento', 'File name', 'algorithm', 'Time spent', 'Memory used', 'Total distance']

# Calcular as médias para cada DataFrame
mean_times_part_1 = calculate_mean_time_by_algorithm_and_file(df_part_1)
mean_times_part_2 = calculate_mean_time_by_algorithm_and_file(df_part_2)
mean_times_part_3 = calculate_mean_time_by_algorithm_and_file(df_part_3)

# Inicializando o dicionário time_usage
time_usage = {
    'sa': [],
    'ts': [],
    'nn': [],
    'ac': [],
    'ga': []
}

# Adicionar médias de cada parte para cada algoritmo
add_means_to_time_usage(mean_times_part_1, time_usage)
add_means_to_time_usage(mean_times_part_2, time_usage)
add_means_to_time_usage(mean_times_part_3, time_usage)

# Garantir que cada algoritmo tenha exatamente 6 valores médios
time_usage_corrected = {alg: [] for alg in time_usage.keys()}
for alg in time_usage.keys():
    if len(time_usage[alg]) == 18:  # 3 execuções, 6 arquivos cada
        time_usage_corrected[alg] = np.mean(np.array(time_usage[alg]).reshape(3, 6), axis=0).tolist()
    elif len(time_usage[alg]) == 12:
        time_usage_corrected[alg] = np.mean(np.array(time_usage[alg]).reshape(3, 4), axis=0).tolist()
    elif len(time_usage[alg]) == 15:
        time_usage_corrected[alg] = np.mean(np.array(time_usage[alg]).reshape(3, 5), axis=0).tolist()
    else:
        print(f"Algoritmo {alg} tem um número incompatível de amostras")

# Verificar o conteúdo do time_usage corrigido
for algorithm, times in time_usage_corrected.items():
    print(f"Algoritmo: {algorithm} - Tempos: {times}")


# Valores de exemplo para n (ajustar conforme necessário)
# n_values = np.array([22, 48, 52, 70, 76, 99])  # inst p
# n_values = np.array([100, 101, 130, 150])  # inst m
n_values = np.array([195, 198, 280, 400, 442])  # inst g

# Obter a complexidade de cada algoritmo
complexities = get_complexity(time_usage_corrected)

# Exibir a complexidade calculada para cada algoritmo
for algorithm, (a, b) in complexities.items():
    print(f"Algoritmo: {algorithm} - Coeficiente a: {a:.2f}, Expoente b: {b:.2f}")
    print(f"Algoritmo: {algorithm} - Complexidade: O(n^{b:.2f})")
