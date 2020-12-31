

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:43:38 2020

@author: thebe
"""
import random
import numpy as np
import timeit
from Graph_Class import Vertex
from Graph_Class import Graph
from Graph_Class import con_graf

from collections import Counter
import matplotlib.pyplot as plt





'''
Randomly switch lights on until g.is_lit() == 1
'''
def switch_until_lit(nr_nodes, nr_edges):
    g = con_graf(nr_nodes,nr_edges)
    #print(g.lit_lists()[2])
    while (g.is_lit() != 1):
        s_g = g.lit_lists()[1][random.randrange(0, nr_nodes)]
        g.switch_on(s_g)
    #print(g.lit_lists()[2])
    return g.lit_lists()[2], g;



'''
Method to print out the lists for an array
'''
def graph_to_list(array):
    new_list_array = []
    for i in range(len(array)):
        new_list_array.append(array[i].lit_lists()[2])
    return new_list_array;






'''
Generates a bunch of different solution maps that are all lit of a certain
amount of nodes and vertices

i.e. lit_maps(10, 4, 3)[0] will return an array showing the lit vertices
lit_maps(10,4,3)[1] will return the graph
'''
def lit_maps(size, nr_nodes, nr_edges):
    pop_graphs = [];
    for i in range(size):
        pop_graphs.append(switch_until_lit(nr_nodes, nr_edges)[1])

    return pop_graphs





'''
Calculates the fitness of each map

i.e. checks_fitness(pop) will return an array with 1 if the map is minimal and 0 if the map is not minimal
'''
def check_fitness(pop_graphs):
    see_if_fit = [];
    for i in range(len(pop_graphs)):

        see_if_fit.append(pop_graphs[i].is_min_lit())
        
    return see_if_fit
            

'''
Reports back the number of minimal graphs
'''
def check_fitness_min(pop_graphs):
    min_fit = 0;
    for i in range(len(pop_graphs)):

        min_fit += pop_graphs[i].is_min_lit()
        
    return min_fit




'''
selects the 48 best individuals
'''
def select_48_best(pop_graphs):
    check = check_fitness(pop_graphs);
    
    fit = []
    new_fit = []
    non_minimal = []
    for i in range(len(pop_graphs)):
        if pop_graphs[i].is_min_lit() == 1:
            fit.append(pop_graphs[i])
        elif pop_graphs[i].is_min_lit() == 0:
            non_minimal.append(pop_graphs[i])
    
    if len(fit) >= 48:
        new_fit = fit[:48]
        #print(check_fitness_min(new_fit))
        #print("num fit", check_fitness_min(new_fit))
    else:
        new_fit = non_minimal[:48 - len(fit)] + fit
        #print("num fit", check_fitness_min(new_fit), len(fit))
        #print(len(non_minimal), len(fit))
    
    return new_fit
            





'''
Crossing over using graphs
'''
def cross_over_graphs(parent_g1, parent_g2):
      import copy
      child_g1 = copy.deepcopy(parent_g1)
      child_g2 = copy.deepcopy(parent_g2)
     
      chrom_length = 2; #want to change this later
     
      # get parent info
      parent_g1_info = parent_g1.lit_lists()[2] 
      parent_g2_info = parent_g2.lit_lists()[2] 
 
     
      for i in range(chrom_length):
          if parent_g2_info[i] == 1:
              child_g1.switch_on(i)
          else:
              child_g1.switch_off(i)
     
      for j in range(chrom_length):
          if parent_g1_info[j] == 1:
              child_g2.switch_on(j)
          else:
              child_g2.switch_off(j)
             
      return child_g1, child_g2




 

'''
48 kids created from the crossing over
'''
def next_gen(fit):
    kids = []
    for i in range(0, 48, 2):
        w = cross_over_graphs(fit[i], fit[i+1])
        kid1, kid2 = w[0], w[1]
        kids.append(kid1)
        kids.append(kid2)
    return kids






'''
Check if each new kid is a solution map
'''
def is_sol(array):
    true_g = [];
    for i in range(len(array)-1):
        true_g.append(array[i].is_lit())
    return true_g






'''
Mutates 4 individuals
'''
def mutates_4_ind(array):
    mutated = []
    for i in range(4):
        a = array[random.randint(1, len(array)-1)];
        #print(a.lit_lists()[2])
        L = len(a.lit_lists()[2])
        r = random.randint(1,L)-1
        if a.lit_lists()[2][r] == 1:
            a.switch_off(r)
        else:
            a.switch_on(r)                           
        mutated.append(a)
    return mutated









'''
  *************************************
  ******** ALGORITHM CODE ********
  *************************************
'''


#Okay, let's start

num_sol_maps = 100;
num_nodes = 4;
num_edges = 3;
num_generations = 50;

sp_graphs = lit_maps(num_sol_maps, num_nodes, num_edges); 
#print(graph_to_list(starting_pop))

#print(sp_graphs)

generations = [0]

minimal = [check_fitness_min(sp_graphs)];
#print("initial", check_fitness_min(sp_graphs))


for i in range(num_generations):
    
    #SELECTION
    
    best = select_48_best(sp_graphs)
    
    np.random.shuffle(best)


    #REPRODUCTION
    #Here are 48 'enfants' from the best 48 individuals using crossing over
    crossed = next_gen(best)
    

    #MUTATION
    #Randomly take 4 from and mutate them from the previous generation
    mutate = mutates_4_ind(sp_graphs)
    
    
    #Add all the populations together
    sp_graphs = best + crossed + mutate

    np.random.shuffle(sp_graphs)
    
    #print("loop", i + 1, check_fitness_min(sp_graphs))
    
    minimal.append(check_fitness_min(sp_graphs))
    generations.append(i + 1)
    
#print("min", minimal)
#print("gen", generations)
    
    
plt.plot(generations, minimal)
plt.xlabel('nombre de generations')
plt.ylabel('nombres de graphes minimale')
plt.grid()

    
    
