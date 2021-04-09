#!/bin/python
"""This is a simple text editor"""
# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




# Create a function to read the data file
def read_data(filename,delimiter=',',starting_row=0):
    """This function reads data from a specified filename.
    The specified filename should point to a .csv file."""
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=delimiter,skip_header=5)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    temperature_data = np.array(all_data[starting_row:,:], dtype=float)
    return temperature_data

def process_data(temperature_data):
    """Given some input temperature data this function converts the second column
    from degrees F to K and appends a new column with that data. """
    # Compute a new column by multiplying column number 1 to Kelvin
    temperature_kelvin = (temperature_data[:,1,None] - 32) * 5/9 + 273

    # Append this new column to the existing temperature_data array
    processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)
    return processed_temperature_data

def plot_data(processed_temperature_data, plot_filename):
    """ Given some input temperature data this function converts the second column
    from degrees F to K and appends a new column with that data. """
    # Create a figure of the processed data
    temperature_figure = plt.figure()
    plt.bar (processed_temperature_data[:,0],
                                processed_temperature_data[:,2],
                                 width=50, color='blue')

    plt.show(block=True)
    temperature_figure.savefig(plot_filename)


def convert_data(filename, output_filename):
    """ Read data from a CSV falled filename, and write this
     data into a Pandas dataframe, and write this dataframe
     into a json file called output_filename. """
    all_data = pd.read_csv(filename, index_col='Date', header=4)
    all_data.info()
    all_data.to_json(output_filename)

def plot():
    """Maine program that reads a dataset and processes it, plots it, and write the
     converted data into a json file"""
    input_file = "110-tavg-12-12-1950-2020.csv"
    plot_file = "temperature-over-time.pdf"
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_filename = os.path.join(data_directory,input_file)
    plot_filename = os.path.join(results_directory,plot_file)
    json_filename = os.path.join(results_directory,json_output_file)

    temperature_data = read_data(input_filename, starting_row=5)
    processed_temperature_data = process_data(temperature_data)
    plot_data(processed_temperature_data, plot_filename)
    convert_data(input_filename, json_filename)

if __name__ == "__main__":
    print(sys.argv)
    plot()
