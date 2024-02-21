import numpy as np

def calculate_mean(data):
""" This function computes the mean of an array.
I: An one dimensional array
O: The mean of the array 
Usage:
data = np.array([0,10,20,30])
mean=calculate_mean(data)"""
	mean=np.mean(data)
	return mean
