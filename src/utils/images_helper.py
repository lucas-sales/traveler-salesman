import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

num_nodes = [52, 101, 195]


def memory_usage_plot():
    # Dados
    memory_usage1 = {
        'Simulated Annealing': [0.203125, 0.2265625, 0.22265625],
        'Nearest Neighbor': [0.00390625, 0.02734375, 0.12109375],
        'Tabu Search': [0.00390625, 0.0390625, 0.23046875],
    }

    memory_usage2 = {
        'Ant Colony': [0.27734375, 17.046875,  14.66796875],
        'Genetic Algorithm': [0.37890625, 2.1171875, 6.54296875]
    }

    # Criação do gráfico
    plt.figure(figsize=(10, 6))

    for algorithm, memory in memory_usage2.items():
        plt.plot(num_nodes, memory, marker='o', label=algorithm)

    # Configurações do gráfico
    plt.xlabel('Número de Nós')
    plt.ylabel('Uso de Memória (MiB)')
    plt.title('Comparação do Uso de Memória de Algoritmos TSP')
    plt.legend()
    plt.grid(True)

    # Exibição do gráfico
    plt.show()


def time_usage_plot():
    time_usage1 = {
        'Simulated Annealing': [0.082409, 0.345311, 0.558787],
        'Tabu Search': [0.169819, 0.515627, 0.984361],
    }
    time_usage2 = {
        'Nearest Neighbor': [18.969058, 133.361888, 490.676619],
        'Ant Colony': [118.626132, 425.567967, 1481.068389],
        'Genetic Algorithm': [48.731099, 141.814880, 352.586174]
    }

    # Criação do gráfico
    plt.figure(figsize=(10, 6))

    for algorithm, memory in time_usage2.items():
        plt.plot(num_nodes, memory, marker='o', label=algorithm)

    # Configurações do gráfico
    plt.xlabel('Número de Nós')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Comparação do tempo de execução de Algoritmos TSP')
    plt.legend()
    plt.grid(True)

    # Exibição do gráfico
    plt.show()


def complexity_plot():
    # Tempos de execução
    time_usage = {
        'Simulated Annealing': [0.082409, 0.345311, 0.558787],
        'Tabu Search': [0.169819, 0.515627, 0.984361],
        'Nearest Neighbor': [18.969058, 133.361888, 490.676619],
        'Ant Colony': [118.626132, 425.567967, 1481.068389],
        'Genetic Algorithm': [48.731099, 141.814880, 352.586174]
    }

    # Função para ajuste de curva polinomial
    def poly_func(n, a, b):
        return a * n ** b

    # Plote os dados e ajuste as curvas
    plt.figure(figsize=(10, 6))

    for algorithm, times in time_usage.items():
        popt, _ = curve_fit(poly_func, num_nodes, times)
        plt.plot(num_nodes, times, 'o', label=f'{algorithm} (dados)')
        plt.plot(num_nodes, poly_func(num_nodes, *popt), '-', label=f'{algorithm} (ajuste: O(n^{popt[1]:.2f}))')

    plt.xlabel('Número de Cidades (n)')
    plt.ylabel('Tempo de Execução (s)')
    plt.yscale('log')
    plt.xscale('log')
    plt.legend()
    plt.title('Complexidade Computacional dos Algoritmos TSP')
    plt.grid(True, which="both", ls="--")
    plt.show()


if __name__ == "__main__":
    # memory_usage_plot()
    # time_usage_plot()
    complexity_plot()
