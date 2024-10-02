from data_helper import extract_data
from math_helper import calculate_total_distance


def get_best_solution(file_name) -> None:
    data_s = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/small_data")
    data_m = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/medium_data")
    data_l = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/large_data")
    files_result = extract_data("/Users/lucassales/Dev/TCC/traveler-salesman/file_results")
    for f in data_l:
        if f['name'] == file_name:
            for r in files_result:
                if r['name'] == str(file_name + '.opt.tour'):
                    print(calculate_total_distance(f["node_coords"], sum(r["tours"], [])))

# Exemplo de uso
# get_best_solution('pr1002')
