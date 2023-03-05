# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 19:15:37 2023

@author: Blaise Ezeokeke
"""

#GRAPH ASSIGNMENT APPLIED DATA SCIENCE

#This analysis the Motives of Murder Data in India between 2001 and 2013

# We begin by importing the libraries: pandas, numpy and matplotlip.

import numpy as np  #numpy is a library for data analysis and computation

import pandas as pd 

import matplotlib.pyplot as plt


# Read the DataFrame, using the Pandas library

motives = pd.read_csv(r"C:/Users/Blaise Ezeokeke/Documents/Applied Data/Murder Motives.csv")

print(motives)

#INSPECTING THE DATAFRAME

print(motives.info()) #This method inspects the data type and missing values

print(motives.shape) #This method checks the number of columns and rows of the DataFrame

print(motives.describe()) #This computes some summary for individual columns

print(motives.isnull().sum()) #This checks whether any value misses

motives = motives.groupby("YEAR").sum() #There is need to group to discover agregates
print(motives)

#COLUMN INDEXING
#Here, I slice the actual columns I will work with

motives = motives[["Personal Vendetta or Enemity", "Casteism", "Communalism", "Political Reasons"]] 

"""
These are the actual columns to visualise. As there are 16 columns in,
it would be easier to slice and use only four. 
"""
print(motives)



#Define a function for graph plotting

def plot_line(axis_x, axis_y, x_label="", y_label ="", title=""):
    
    """
    A function to create a line graph using Matplotlip

    Summary:
    axis_x - These are value in the x-axis
    y_data - These are values in the y-axis
    x_label - label for the x-axis
    y_label - label for the y-axis
    title - title of the plot


    No Returns
    
    """
    
    plt.plot(axis_x, axis_y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
 
    #This is the legend
    plt.legend()
        
    #The line graph is saved as a png file
        
    plt.savefig("graph.png")
      
   #Plotting for Personal Vendetta or Enemity against 
plot_line(motives.index, motives["Personal Vendetta or Enemity"], x_label="YEAR",
         y_label="Occurences", title="Motives of Murder in India 2001 to 2013",)


#Casteism against YEAR plot
plot_line(motives.index,motives['Casteism'],
          x_label='YEAR', y_label='Occurence',
          title='Motives of Murder in India 2001 to 2013')

#Communalism against YEAR plot
plot_line(motives.index,motives['Communalism'],
          x_label='YEAR', y_label='Occurence',
          title='Motives of Murder in India 2001 to 2013')


#"Political Reasons" against YEAR plot
plot_line(motives.index,motives["Political Reasons"],
          x_label='YEAR', y_label='Occurence',
          title='Motives of Murder in India 2001 to 2013')
plt.show()

#Computing the combined cases

motives_combined = np.sum(motives, axis=0)
print(motives_combined)


#Pie Chart function for the total motives

def pie_plot(labels,values):
    # Plotting the pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
   
    # inputting the title
    ax.set_title("Motives of Murder in India 2001 to 2013")
   
    #Data for motive and occurences
    
labels=["Personal Vendetta or Enemity", "Casteism", "Communalism", "Political Reasons"]
values=[150795, 1752,  2184, 5682]

pie_plot(labels,values)
plt.savefig("pie_plot.png")
    
plt.show()
    
    
   #Plotting for Bar chart
labels = ["Personal Vendetta or Enemity", "Casteism", "Communalism", "Political Reasons" ]
values = [150795, 1752, 2184,5682 ]

# Creating bar chart
plt.bar(labels, values, color='green')

    

# Seting axis labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Motives of Murder in India 2001 to 2013')
 
# Show plot
plt.show() 

        
        
    
        
    

