import pandas as pd
import numpy as np

# Dados
data = {
    'Ulysses22': {
        'nn': {'tempo': [0.006, 0.005, 0.005], 'distancia': [86.91, 86.91, 86.91]},
        'aco': {'tempo': [0.73, 0.74, 0.72], 'distancia': [77.06, 76.81, 75.97]},
        'ts': {'tempo': [0.06, 0.05, 0.06], 'distancia': [93.38, 82.03, 94.34]},
        'ga': {'tempo': [19.66, 19.52, 20.84], 'distancia': [115.58, 133.98, 120.60]},
        'sa': {'tempo': [0.02, 0.03, 0.03], 'distancia': [77.02, 91.36, 93.16]}
    },
    'Att48': {
        'nn': {'tempo': [0.10, 0.10, 0.10], 'distancia': [39236.88, 39236.88, 39236.88]},
        'aco': {'tempo': [3.01, 3.05, 3.05], 'distancia': [38786.50, 37686.56, 38360.31]},
        'ts': {'tempo': [0.20, 0.19, 0.20], 'distancia': [64901.00, 63755.50, 62395.41]},
        'ga': {'tempo': [54.04, 50.62, 50.84], 'distancia': [114476.47, 120666.54, 115400.97]},
        'sa': {'tempo': [0.10, 0.10, 0.10], 'distancia': [64876.10, 54704.75, 53177.38]}
    },
    'Berlin52': {
        'nn': {'tempo': [0.07, 0.07, 0.08], 'distancia': [8182.19, 8182.19, 8182.19]},
        'aco': {'tempo': [3.54, 3.59, 3.58], 'distancia': [9100.75, 8134.04, 8671.88]},
        'ts': {'tempo': [0.13, 0.13, 0.12], 'distancia': [13635.72, 13240.02, 14073.38]},
        'ga': {'tempo': [44.60, 45.82, 43.78], 'distancia': [23677.22, 23528.93, 21884.90]},
        'sa': {'tempo': [0.07, 0.06, 0.06], 'distancia': [14061.34, 13937.97, 12564.14]}
    },
    'Pr76': {
        'nn': {'tempo': [0.40, 0.40, 0.40], 'distancia': [130921.00, 130921.00, 130921.00]},
        'aco': {'tempo': [7.59, 7.33, 7.41], 'distancia': [131068.41, 129765.58, 125742.28]},
        'ts': {'tempo': [0.30, 0.29, 0.32], 'distancia': [150779.86, 150779.86, 150779.86]},
        'ga': {'tempo': [92.81, 97.0, 82.97], 'distancia': [499658.30, 491325.74, 488365.77]},
        'sa': {'tempo': [0.16, 0.16, 0.15], 'distancia': [270647.02, 265099.28, 279423.43]}
    },
    'Gr96': {
        'nn': {'tempo': [0.43, 0.46, 0.44], 'distancia': [603.30, 603.30, 603.30]},
        'aco': {'tempo': [12.04, 11.54, 11.64], 'distancia': [633.72, 608.44, 610.78]},
        'ts': {'tempo': [0.21, 0.22, 0.22], 'distancia': [748.42, 720.21, 723.53]},
        'ga': {'tempo': [86.80, 88.34, 86.76], 'distancia': [2830.79, 2910.86, 2848.32]},
        'sa': {'tempo': [0.12, 0.11, 0.12], 'distancia': [1685.72, 1609.80, 1491.65]}
    }
}


# Função para calcular média, variância e desvio padrão
def calcular_metricas(valores):
    media = np.mean(valores)
    variancia = np.var(valores)
    desvio_padrao = np.std(valores)
    return media, variancia, desvio_padrao


# Dicionário para armazenar os resultados por algoritmo
resultados = {}

# Iterar sobre os dados e calcular as métricas para cada algoritmo
for conjunto, algoritmos in data.items():
    for algoritmo, valores in algoritmos.items():
        if algoritmo not in resultados:
            resultados[algoritmo] = {'tempo': [], 'distancia': []}
        resultados[algoritmo]['tempo'].extend(valores['tempo'])
        resultados[algoritmo]['distancia'].extend(valores['distancia'])

# Imprimir os resultados para cada algoritmo
for algoritmo, valores in resultados.items():
    print(f"Algoritmo: {algoritmo}")
    for metrica, dados in valores.items():
        media, variancia, desvio_padrao = calcular_metricas(dados)
        print(f"  {metrica.capitalize()}:")
        print(f"    Média: {media:.2f}")
        print(f"    Variância: {variancia:.2f}")
        print(f"    Desvio Padrão: {desvio_padrao:.2f}")
    print()
