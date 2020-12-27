# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:19:55 2020

@author: Asus
"""
from Graph_Class import Graph
from Search_optimal import f_lit_con_graf
from Search_optimal import search_min
from Search_optimal import naive_search

import random
import timeit

g = f_lit_con_graf(100,220) 




code_to_test1 = """

from Graph_Class import Graph
from Search_optimal import f_lit_con_graf
from Search_optimal import search_min
from Search_optimal import naive_search

import random

g = f_lit_con_graf(300,1000) 

naive_search(g)

"""

code_to_test2 = """

from Graph_Class import Graph
from Search_optimal import f_lit_con_graf
from Search_optimal import search_min
from Search_optimal import naive_search

import random

g = f_lit_con_graf(300,1000) 

search_min(g)

"""

elapsed_time1 = timeit.timeit(code_to_test1, number=10)/10
elapsed_time2 = timeit.timeit(code_to_test2, number=10)/10


print(elapsed_time1, 'vs', elapsed_time2)


