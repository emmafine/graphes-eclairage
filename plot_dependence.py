# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:24:14 2020

@author: Asus
"""

from Graph_Class import Graph
from Search_optimal import f_lit_con_graf
from Search_optimal import search_min

from Search_optimal import  search_min_plot

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

######################## Plot cute dependency

def plot_sol(V):
    X = []
    Y = []
    for i in range(2*V, (V-1)*V//2, V//2 ):
        gr = f_lit_con_graf(V, i)
        X.append(search_min_plot(gr)[1])
        Y.append(search_min_plot(gr)[2])
        
    return X,Y

V = 110

t = np.array(plot_sol(V)[0])
s = np.array(plot_sol(V)[1])

s1 =  (t-2)*V/t  #1 + np.sin(2 * np.pi * t)


fig, ax = plt.subplots()
ax.plot(t, s, label = 'data')
ax.plot(t,s1, label = '(Avg-2)Nr_Vert/Avg')


ax.set(xlabel='Avg nr of connections', ylabel=' Nr of lamps in a min lit graph',
       title='Dependence for Nr_Vert =110')
ax.grid()

fig.savefig("test.png")
plt.legend()
plt.show()

############################################################