# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""

# Imports the csv function to load a file & path and also save a file to a specified folder.

import csv

# The following function loads a specific cvs file, file path, and makes it accessible within the application.

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


# The save_csv function exports a file list as a csv file to a specified folder.

def save_csv(csvpath, data, header=None):
    """ this functions saves a CSV file from a given path provided.
    """
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)