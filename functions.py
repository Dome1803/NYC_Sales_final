"""
This module provides helper methods to analyze sales
"""

# Imports
import pandas as pd


def read_csv(file_name):
    """
    This function reads a CSV file in German format.
    :param file_name: The file name.
    :return: A data frame with the contents.
    """
    return pd.read_csv(file_name, sep=",")

def read_german_csv(file_name):
    """
    This function reads a CSV file in German format.
    :param file_name: The file name.
    :return: A data frame with the contents.
    """
    return pd.read_csv(file_name, sep=";")


def to_csv(file_name, data_frame):
    """
    This function saves a CSV file.
    :param file_name: The file name.
    :param data_frame: The data frame.
    :return: A CSV file with "," as the separator.
    """
    data_frame.to_csv(file_name, sep=",", index=False)

def to_german_csv(file_name, data_frame):
    """
    This function saves a CSV file in German format.
    :param file_name: The file name.
    :param file_name: The data frame.
    :return: A CSV file with ";" as the separator and "," as decimal mark.
    """
    data_frame.to_csv(file_name, sep=";", decimal=",", index=False)

def to_datetime(data_frame):
    """
    This function changes format to datetime.
    :param data_frame: The data frame.
    :return: A column of the data frame in datetime format.
    """
    pd.to_datetime(data_frame)

def to_qm(value):
    """
    This function changes squarefoot to squaremeter.
    :param value: The values of a specific column of the data frame.
    :return: The result of the calculation.
    """
    result = value*0.092903
    return result


