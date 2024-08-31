import numpy as np
from scipy.optimize import curve_fit

# Dados fornecidos
n_values = np.array([52, 101, 195])

# Dados
time_usage = {
    'Simulated Annealing': [0.082409, 0.345311, 0.558787],
    'Tabu Search': [0.169819, 0.515627, 0.984361],
    'Nearest Neighbor': [18.969058, 133.361888, 490.676619],
    'Ant Colony': [118.626132, 425.567967,  1481.068389],
    'Genetic Algorithm': [48.731099, 141.814880, 352.586174]
}


# Função polinomial para ajuste de curva
def poly_func(n, a, b):
    return a * n**b


# Função para obter a complexidade de cada algoritmo
def get_complexity(time_usage):
    complexities = {}
    for algorithm, times in time_usage.items():
        popt, _ = curve_fit(poly_func, n_values, times)
        a, b = popt
        complexities[algorithm] = (a, b)
    return complexities

# Obter a complexidade para cada algoritmo
complexities = get_complexity(time_usage)

# Exibir os resultados
for algorithm, (a, b) in complexities.items():
    print(f"{algorithm}: a = {a:.6f}, b = {b:.6f}")