
# In this program it is intended to solve the TSP problem 
# using Genetic Algorithm

from random import *
import math as math
from matplotlib import pyplot as plt

# height and width for the map

height  =600
width = 600

min_distance = 2e9 #curr best

# min_distance represents the minimum distance that need to be travelled in current population

best_ever = min_distance+1

# best_ever is the minimum distance traveled in all the population till a given instance

# number of cities to be visited
num_cities =10
population_size = num_cities*6

# the distance that need to be travelled to visit all cities in a given order
def calc_distance(cities,order):

    total_sum = 0
    prev = [0,0]
    for x in order:

        #assuming starting from 0,0
        curr  = cities[x]
        total_sum+= math.dist(prev,curr)
        prev = curr 
    return total_sum

# swaps elements at indexes a and b in the array arr
def swap(arr,a,b):
    c = arr[b]
    arr[b] = arr[a]
    arr[a] = c
    return

# shuffles the given array with given frequency

def shuffle_1(arr,freq=10):

    n = len(arr)

    for i in range(freq):
        swap(arr,i%n,randint(0,n-1))

































