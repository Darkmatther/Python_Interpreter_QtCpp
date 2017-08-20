# Author: Matthieu Kieffer
# https://github.com/Darkmatther
""" 
    Description: 
    A simple program that reads an input .csv file, 
    loads its content into a numpy array, 
    do some operations on it (here rescaling) 
    and then print the resulting array into an output .csv file
"""


import os 
import sys
import numpy as np

input = "inputFile.csv"
output = "outputFile.csv"


def read_file(input_file_name):
    """Read an input file and convert it into a data matrix"""

    #Test the validity of the input file
    try:
        input_file = open(input_file_name, 'r')
        file_size = os.stat(input_file_name)
        if file_size == 0:
            input_file.close()
            print "Error! The input file ", input_file_name, " is empty. Please lauch the program on a non-empty input file."
            return np.array([]) #returns an empty matrix
    except:
        print "Error! The entered input file does not exist. Please re-check the file name."
        return np.array([]) #returns an empty matrix

    #Copy data from the input file into a data matrix
    data = []
    for line in input_file:
        new_data = map(float, line.split(","))
        data.append(new_data)
    input_file.close()
    data_matrix = np.array(data)
    print "Input file read correctly!"
	
    return data_matrix

	

def scale_data(input_data):
    """Scale input data following to the formula: x_scaled = (x-mean(x))/stdev(x)"""

    mean_data = np.mean(input_data, axis=0)

    stdev_data = np.std(input_data, axis=0)

    scaled_data = np.copy(input_data)

    for data in scaled_data:
        for i, feature in enumerate(data):
            data[i] = (data[i] - mean_data[i]) / stdev_data[i]

    return scaled_data

	

def main():

    input_file_name = input
    output_file_name = output

    #Get data from the input file
    input_data = read_file(input_file_name)
    if len(input_data) == 0:
        return 0

    #Scale data with respect to mean and standard deviation values
    scaled_data = scale_data(input_data)

    # ...
    # Do some other operations on the numpy array
    # ...

    #Write the rescaled data into the output file
    np.savetxt(output, scaled_data, fmt='%.6f', delimiter=",")
    print "Output file has been written at the following location : ", os.getcwd()



if __name__ == "__main__":
    main()
