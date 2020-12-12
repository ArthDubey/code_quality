import os
from .complete_check import completeCheck
from .reporting_module.report import summaryFromScore
from termcolor import colored
from .reporting_module.consistent_padding_line import consistentPadding


def allPythonFilesOfADir(dirPath: str) -> list:
    all_python_files = []

    def recursiveSearch(path):
        if os.path.isfile(path):
            if path[-3:] == ".py":
                all_python_files.append(path)
            return
        childrenFiles = os.listdir(path)
        for child in childrenFiles:
            childPath = os.path.join(path, child)
            recursiveSearch(childPath)
        return
    recursiveSearch(dirPath)
    return all_python_files


def aggregateScore(dirPath: str) -> dict:
    print(consistentPadding("Starting Quality Test Session"))
    print()
    all_python_files = allPythonFilesOfADir(dirPath)

    total = {
        "Readability Score": 0,
        "Document Size Score": 0,
        "Redundancy Check Score": 0,
        "Function size score": 0
    }

    if not all_python_files:
        return total
    keys = list(total.keys())
    for filepath in all_python_files:
        print(
            "---> executing checks on " +
            colored(filepath, 'cyan')
        )
        score = completeCheck(filepath)
        for key in keys:
            total[key] += score[key]

    for key in keys:
        total[key] /= len(all_python_files)

    summaryFromScore(total)
    return total
