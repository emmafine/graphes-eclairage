# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:19:55 2020

@author: Asus
"""
from Graph_Class import Graph
from Graph_Class import con_graf
from Search_optimal import f_lit_con_graf
from Search_optimal import search_min
from Search_optimal import simple_search

import random
import timeit

g = con_graf(400,600) 




code_to_test1 = """

from Graph_Class import Graph
from Graph_Class import con_graf
from Search_optimal import f_lit_con_graf
from Search_optimal import search_min
from Search_optimal import simple_search

import random

g = con_graf(400,600) 

simple_search(g)

"""

code_to_test2 = """

from Graph_Class import Graph
from Graph_Class import con_graf
from Search_optimal import f_lit_con_graf
from Search_optimal import search_min
from Search_optimal import simple_search

import random

g = con_graf(400,600) 

search_min(g)

"""

elapsed_time1 = timeit.timeit(code_to_test1, number=1)/1
elapsed_time2 = timeit.timeit(code_to_test2, number=1)/1


print('Simple method',elapsed_time1,'s', 'vs', elapsed_time2,'s','Improved method')





