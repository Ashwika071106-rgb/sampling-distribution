import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

import statistics
import random

df = pd.read_csv("sampling_distribution/temp_data.csv")
data = df['temp'].tolist()

# code to show the plot of raw data
#fig = ff.create_distplot([data],["temp"], show_hist = False)
#fig.show()

population_mean = statistics.mean(data)
print("Population Mean :- ",population_mean)

pop_std_deviation = statistics.stdev(data)
print("Population Standard Deviation :- ",pop_std_deviation)

#code to find mean and std deviation of 100 data points
#dataset = []
#for i in range(0, 100):
    #random_index= random.randint(0,len(data))
    #value = data[random_index]
    #dataset.append(value)
#mean = statistics.mean(dataset)
#std_deviation = statistics.stdev(dataset)

#print("Mean of sample:- ",mean)
#print("std_deviation of sample:- ",std_deviation)

##  code to find the mean of 100 data points 1000 times and plot it
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    deviation = statistics.stdev(mean_list)
    print("Standard Deviation of sampling distribution :- ",deviation)

standard_deviation()