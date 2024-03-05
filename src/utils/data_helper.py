import os
import tsplib95


def extract_data(path: str):
    problem_list = []
    arr = os.listdir(path)
    for file in arr:
        problem = tsplib95.load(path + "/" + file)
        problem_list.append(problem.as_dict())
    return problem_list

