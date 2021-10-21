"""this file is to calculate means and OLS for Campus.csv"""

import pandas as pd

import numpy as np

# function to extract variable means
dataframe = r"~/OneDrive/Documents/Python/406homework/PS3delaroca/campus.csv"

print(dataframe)


def extract_variable_means(dataset_filename: str):
    '''Calculates the mean values of the number of total campus crimes, employed
police officers, and total college enrollment'''
    dataframe = pd.read_csv(dataset_filename)
    crime_mean = sum(dataframe["crime"]) / len(dataframe["crime"])
    police_mean = sum(dataframe["police"]) / len(dataframe["police"])
    enroll_mean = sum(dataframe["enroll"]) / len(dataframe["enroll"])
    means = {"mean crime:": crime_mean, "mean police:": police_mean,
             "mean enrolled:": enroll_mean}
    return means


# test
# extract_variable_means(dataframe)


def extract_estimator_and_covariance(dataset_filename: str):
    """Calculates the ols estimator vector"""
    dataframe = pd.read_csv(dataset_filename)
    dataframe = dataframe.dropna(axis=0, how="any")
    dataframe["β0"] = 1
    y_vector = dataframe["lcrime"]
    dataframe = dataframe[["lenroll", "β0"]]
    beta_vector = np.dot(np.linalg.inv(np.dot(np.transpose(dataframe),
                         dataframe)), np.dot(np.transpose(dataframe),
                         y_vector))
    return beta_vector


print(extract_estimator_and_covariance(dataframe))
