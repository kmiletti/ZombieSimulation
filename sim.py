from Person import Person
from Susceptible import Susceptible
from Infected import Infected
from Recovered import Recovered

# This simulation is meant model a zombie apocalypse.
# This uses the original SIR model, OOP, probability, and plotting/data visualization methods.

    #add the following to set up function
    # print("This simulation models a zombie virus outbreak on an island\n "
    # "Below you will be asked to enter\n 1. the number of susceptible and infected\n 2. the rates of infectino and recovery\n and 3. the size of the island."
    # S = input("Enter number of susceptibles.")
    # I = input("Enter number of infected.")
    # etc


def setup():

    s= 37
    i= 3
    ir = .1
    rr = .01

    s_count = [s] #value changes will be added to list
    i_count = [i]
    r_count = []

    # create susceptible population, store in a list
    s_instances = []
    s_instances = [Susceptible(str(s), 0, 0) for i in range(0, s)]

    #create infected population, store in a list
    i_instances = []
    i_instances = [Infected(str(i), 0,0) for i in range(0, i)]

    #create island
    matrix_size = 0

    # return s_list
    # return i_list
    # return matrix_size


def simulation(s_instances, i_instances, matrix_size):
    n=1
    end = False
    while end != True:
        if s_instances[n] <= 0:
            end = True

    # return the three lists of counts

def plot(s_list, i_list, z_list):
    '''Takes three lists, which kept track of changes in population'''

    t_list = []
    for t in 40:
        t_list += t

    #figure out matplotlib, and plot etc.

