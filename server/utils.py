import os
import numpy as np


def get_files_by_dir(dir_path: str = './') -> list[str]:
    """
    Returns the file paths in a directory.

    :param dir_path: str: directory path
    :returns: list[str]
    """
    assert os.path.isdir(dir_path), 'dir_path must be a directory'
    return [[file for file in files] for _, _, files in os.walk(dir_path)][0]


def get_codes(files: list[str]) -> list[str]:
    """
    Returns the codes in a list of files.

    :param files: list[str]
    :returns: list[str]
    """
    assert len(files) > 0, 'length of files must be greater than 0'
    codes = []
    for file in files:
        data = open(file, 'rt', encoding='UTF8')
        codes.append(data.read())
        data.close()
    return codes


def get_z_scores(metrics: list[float]) -> list[float]:
    """
    Returns the z-scores of a list of metrics.

    :param metrics: list[float]
    :returns: list[float]
    """
    assert len(metrics) > 0, 'length of metrics must be greater than 0'
    mean = sum(metrics) / len(metrics)
    std = np.std(metrics)
    return [round((x - mean) / std, 3) for x in metrics]
