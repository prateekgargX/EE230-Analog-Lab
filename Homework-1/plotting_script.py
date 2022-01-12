import matplotlib.pyplot as plt
import numpy as np
import math

#_______________________________________________________________________________________________________________
filename     = "RC_Int"              #filename : This is name of the file containing the x and y values
Plot_Title   =  "This is a plot title"
x_axis_label = "x_axis_label"
y_axis_label = "y_axis_label"
number_of_curves_in_plot = 1
legend_list = ["a"]
LOG_OF_X = True                         #LOG_OF_X : x axis will be logarithmic if LOG_OF_X is 'True'
is_first_order_derivative = True
#_______________________________________________________________________________________________________________

x_axis_colum_number = 1                     #this is column no. from which actual data start. It lowest value is 0.
y_axis_column_start = x_axis_colum_number+1  #After x axis column, all further columns will be y axis columns


global readings
global x_readings
global y_readings

x_readings = []
y_readings = []

numbers =['0','1','2','3','4','5','6','7','8','9']

#This function read the file and returns the x and y axis values
def read_file(axis_index):
    axis_readings = []
    readings_file = open(filename, "r");

    # read file line by line
    for x in readings_file:

        if x == "":
            #skip blank lines
            continue
        elif not(x[0] in numbers):
            # skip  lines which do not contain readings
            continue

        # remove new line character from each
        x = x.replace("\n", "")

        # seperate three numbers from line -> Index x_value y_value
        readings = [float(d) for d in x.split()]
        #print("readings-->",readings)
        try:
            axis_readings.append(readings[axis_index])
        except:
            print("________________________________________________________________________________________")
            print("***************Column number mismatch Error*************")
            print("Column number mismatch Error: Number of curves in the given output file are less than number_of_curves_in_plot")
            print("________________________________________________________________________________________")
            exit(0)

    return axis_readings



def first_order_derivative(x_array, y_array):

    x_array_der = np.zeros(len(x_array) - 1)
    y_array_der = np.zeros(len(x_array) - 1)

    y_array_der = np.diff(y_array) / np.diff(x_array)
    #print("len(y_array_der)=", len(y_array_der[0]))

    for i in range(len(x_array) -1):
        x_temp = (x_array[i] + x_array[i + 1]) / 2
        x_array_der[i] = x_temp

    #print("len(x_array_final)=", len(x_array_final))

    return  x_array_der,y_array_der




if __name__ == '__main__':

    #check whether number of curves are equal to names filled legend_list
    if not (number_of_curves_in_plot == len(legend_list)):
        print("________________________________________________________________________________________")
        print("***************Length mismatch Error*************")
        print("Length mismatch Error: number_of_graphs_in_plot and length of legend_list must be the same")
        print("________________________________________________________________________________________")
        exit(0)


    #Read file and get x and y axis values in following two arrays
    x_readings = read_file(x_axis_colum_number)

    #print("x_readings-->",x_readings)

    y_readings = []
    for column in range(y_axis_column_start, number_of_curves_in_plot + y_axis_column_start):
        y_readings.append(read_file(column))
        #print("y_readings==",y_readings)


    #print(x_readings,"-",y_readings)

    x_array = np.array(x_readings)
    y_array = np.array(y_readings)

    x_array_final = np.zeros(len(x_readings) - 1)
    y_array_final = np.zeros(len(x_readings) - 1)
    # derivative
    if is_first_order_derivative:
        x_array_final,y_array_final= first_order_derivative(x_array, y_array)
    else:
        x_array_final = x_array
        y_array_final = y_array



    #Plot all graphs in single plot
    for column in range(0, number_of_curves_in_plot):
        plt.plot(x_array_final , y_array_final[column],label = legend_list[column])

    plt.title(Plot_Title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)

    # For lagarithmic X axis
    if (LOG_OF_X):
        plt.xscale("log")

    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()
