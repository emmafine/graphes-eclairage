# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:52:50 2020

@author: Asus
"""

#from Graph_Class import Vertex
from Graph_Class import Graph
import random
from math import factorial

g = Graph()
g.add_edge(1, 2,1,1)

def f_lit_con_graf(nr_nodes,nr_edges):
    """  
    spawning a connected graph with nr_nodes nodes 
                                and nr_edges edges
        nr_edges in [nr_nodes - 1, nr_nodes*(nr_nodes-1)/2 ]
    """
    if nr_edges < nr_nodes-1 or nr_edges > nr_nodes*(nr_nodes-1)/2:
        print('nr_edges not in [nr_nodes - 1, nr_nodes*(nr_nodes-1)/2 ]')
        return 0

    fop = Graph()
    fop_l = []
    fop.add_vertex(0, 1)
    for i in range(1,nr_nodes):
        r = random.choice(list(fop.vert_dict.keys()))
        fop.add_vertex(i, 1)
        fop.add_edge(i,r)
        fop_l.append((i,r))
        fop_l.append((r,i))
        
        
    for i in range(nr_nodes-1, nr_edges):
        fr = random.choice(list(fop.vert_dict.keys()))
        to = random.choice(list(fop.vert_dict.keys()))
        while to == fr:
            to = random.choice(list(fop.vert_dict.keys()))
        
        while (fr,to) in fop_l:
            fr = random.choice(list(fop.vert_dict.keys()))
            to = random.choice(list(fop.vert_dict.keys()))
            while to == fr:
                to = random.choice(list(fop.vert_dict.keys()))
        
        fop.add_edge(fr, to)
        fop_l.append((fr,to))
        fop_l.append((to,fr))
    return fop


def simulated_annealing(g):
    adj_dic = {}
    ##switching leafs off and counting the edges each node has
    M = 0
    m = 10**1000
    S = 0
    j = 0
    for i in g.vert_dict.keys():
        l = len(g.vert_dict[i].adjacent)
        adj_dic[i] = len(g.vert_dict[i].adjacent)
        if l > M:
            M = l
        if l < m:
            m = l
        S = S + l
        j+=1
        
        if len(g.vert_dict[i].adjacent) == 1:
            g.vert_dict[i].light = 0
    
    Avg = S/j
    
    
    ###create the lights_list
    for i in range(10):
        r = random.choice(list(g.vert_dict.keys()))
        if adj_dic[r] < Avg:
            if random.random() > 0.1:
                g.switch_off(r)
                
        
        while g.is_lit() ==0:
                r = random.choice(list(g.vert_dict.keys()))
                g.switch_on(r)
        
        
        while g.is_min_lit() == 0:
            
            r = random.choice(list(g.vert_dict.keys()))
            if adj_dic[r] < Avg:
                if random.random() > 0.1:
                    g.switch_off(r)
            else:
                if random.random() > 0.5:
                    g.switch_off(r)
            
            
            
            while g.is_lit() ==0:
                r = random.choice(list(g.vert_dict.keys()))
                g.switch_on(r)
        

# def simulated_annealing_1(g):
#     # adj_dic = {}
#     # ##switching leafs off and counting the edges each node has
#     # M = 0
#     # m = 10**1000
#     # S = 0
#     # j = 0
#     # for i in g.vert_dict.keys():
#     #     l = len(g.vert_dict[i].adjacent)
#     #     adj_dic[i] = len(g.vert_dict[i].adjacent)
#     #     if l > M:
#     #         M = l
#     #     if l < m:
#     #         m = l
#     #     S = S + l
#     #     j+=1
        
#     #     if len(g.vert_dict[i].adjacent) == 1:
#     #         g.vert_dict[i].light = 0
    
#     # Avg = S/j
    
    
#     ###create the lights_list
    
#     while g.is_min_lit() == 0:
#         r = random.choice(list(g.vert_dict.keys()))
#         if g.vert_dict[r].light ==1:
#             if random.random() > 0.1:
#                 g.switch_off(r)
            
#        while g.is_lit() ==0:
#            r = random.choice(list(g.vert_dict.keys()))
#            if g.vert_dict[r].light ==0:
#                g.switch_on(r)
    
    
#     return g
            




def simulated_annealing_2(g):
    adj_dic = {}
    ##switching leafs off and counting the edges each node has
    M = 0
    m = 10**1000
    S = 0
    j = 0
    for i in g.vert_dict.keys():
        l = len(g.vert_dict[i].adjacent)
        adj_dic[i] = len(g.vert_dict[i].adjacent)
        if l > M:
            M = l
        if l < m:
            m = l
        S = S + l
        j+=1
        
        if len(g.vert_dict[i].adjacent) == 1:
            g.vert_dict[i].light = 0
    
    Avg = S/j
    
    
    ###create the lights_list

    r = random.choice(list(g.vert_dict.keys()))
    if g.vert_dict[r] ==1:
            
        if adj_dic[r] < Avg:
            if random.random() > 0.2:
                g.switch_off(r)
        else:
            if random.random() >0.7:
                g.switch_off(r)
        
    while g.is_lit() ==0:
        r = random.choice(list(g.vert_dict.keys()))
        g.switch_on(r)
        
    return g







def search_min(g):
    adj_dic = {}
    ##counting the edges each node has
    M = 0
    m = 10**1000
    S = 0
    j = 0
    for i in g.vert_dict.keys():
        l = len(g.vert_dict[i].adjacent)
        adj_dic[i] = len(g.vert_dict[i].adjacent)
        if l > M:
            M = l
        if l < m:
            m = l
        S = S + l
        j+=1
        
        # if len(g.vert_dict[i].adjacent) == 1:
        #     g.vert_dict[i].light = 0
    
    Avg = S/j
    print('avg = ', Avg)
    print('m=',m)
    print('M=',M)
    if Avg == m:
        while g.is_min_lit() == 0:
            r = random.choice(list(g.vert_dict.keys())) #complexity???? O(n)
            if g.vert_dict[r].light == 1:
                if adj_dic[r] <= Avg:
                    # p = 0.1 + 0.4/b-a (x-a)
                    if random.random() >0.1 + (0.4/(Avg-m +1))*(adj_dic[r]-m):
                        g.vert_dict[r].light =0
                # elif adj_dic[r] > Avg:
                #     #p = 0.5 + 0.4/(c-b) (x-b)
                #     if random.random() > 0.5 + ((0.4)/(M-Avg))*(adj_dic[r]- Avg):
                #         g.vert_dict[r].light = 0
        
            if g.is_lit() == 0:
                g.vert_dict[r].light = 1
        
    
    while g.is_min_lit() == 0:
        r = random.choice(list(g.vert_dict.keys())) #complexity???? O(n)
        if g.vert_dict[r].light == 1:
            if adj_dic[r] <= Avg:
                # p = 0.1 + 0.4/b-a (x-a)
                if random.random() >0.1 + (0.4/(Avg-m))*(adj_dic[r]-m):
                    g.vert_dict[r].light =0
            elif adj_dic[r] > Avg:
                #p = 0.5 + 0.4/(c-b) (x-b)
                if random.random() > 0.5 + ((0.4)/(M-Avg))*(adj_dic[r]- Avg):
                    g.vert_dict[r].light = 0
        
        if g.is_lit() == 0:
            g.vert_dict[r].light = 1
    print(g.how_many_lights())
    return g








fop = Graph()

fop.add_vertex(0, 1)
fop.add_vertex(1, 1)
fop.add_vertex(2, 1)
fop.add_vertex(3, 1)
fop.add_vertex(4, 0)
fop.add_vertex(5, 1)


fop.add_edge(0, 1)
fop.add_edge(0, 2)
fop.add_edge(0, 3)
fop.add_edge(0, 4)
fop.add_edge(4, 5)
fop.add_edge(4, 3)
fop.add_edge(2, 3)
fop.add_edge(2, 5)
fop.add_edge(1, 5)
fop.add_edge(1, 3)




