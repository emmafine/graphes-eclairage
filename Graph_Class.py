# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:17:20 2020

@author: Asus
"""
import random

class Vertex:
    def __init__(self, node):
        self.id = node
        self.light = 1
        self.adjacent = []

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbour(self, neighbour):
        if neighbour not in self.adjacent:
            self.adjacent.append(neighbour)

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    
    def swtich_on(self):
        self.light = 1
        
    def switch_off(self):
        self.light = 1

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, light):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        self.vert_dict[node].light = light
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, frm_l = random.randrange(2), to_l= random.randrange(2)):
        if frm not in self.vert_dict:
            self.add_vertex(frm,frm_l)
        if to not in self.vert_dict:
            self.add_vertex(to,to_l)

        self.vert_dict[frm].add_neighbour(self.vert_dict[to])
        self.vert_dict[to].add_neighbour(self.vert_dict[frm])

    def get_vertices(self):
        return self.vert_dict.keys()
    
    def how_many_lights(self):
        count = 0
        for node in self.vert_dict.keys():
            if self.vert_dict[node].light ==1:
                count= count+1
        return count
    
    def lit_dict(self):
        lit_dict = {}
        for node in self.vert_dict.keys():
            lit_node = 0
            lit_neighbour = 0
            for neighbour in self.vert_dict[node].adjacent:
            #for neighbour in self.vert_dict[node].adjacent.keys():
                if neighbour.light == 1:
                    lit_neighbour = 1
            if self.vert_dict[node].light == 1 or lit_neighbour ==1:
                lit_node = 1
            else:
                lit_node = 0
            lit_dict[node] = lit_node
            
        
        return lit_dict
    
    def is_lit(self):
        lit_dict = self.lit_dict()
        if 0 in lit_dict.values():
            return 0
        else:
            return 1
    
    
    def is_opti_lit(self):
        ok = 1
        if self.is_lit() == 0:
            return 0
        for node in self.vert_dict.keys():
            if len(self.vert_dict[node].adjacent) == 1:
                if self.vert_dict[node].light == 1:
                    ok = 0
        for node in self.vert_dict.keys():
            if self.vert_dict[node].light == 1:
                self.vert_dict[node].light = 0
                if self.is_lit() == 1:
                    ok = 0
        if ok == 0:
            return 0
        else:
            return 1
        

            
def graf(no_nodes, no_edges):
    g = Graph()
    vert_list = [i for i in range(no_nodes)]
    for i in range(no_nodes):
        g.add_vertex(i, random.randrange(2))
    
    for i in range(no_edges):
        frm = random.choice(vert_list)
        c = random.choice(vert_list)
        while c == frm:
            c = random.choice(vert_list)
        to = c
        g.add_edge(frm, to)
    return g

def fake_con_graf(nr_edges):
    #creates a connected graph
    #it assigns random values for the lit condition (0 or 1)
    #to assign specific values use the code
    #g.add_edge(random.randrange(nr_edges+1),random.randrange(nr_edges+1),1,1)
    #instead of 1,1 name the values you wish; 
    g = Graph()
    for i in range(nr_edges):
        frm = random.randrange(nr_edges+1)
        to = random.randrange(nr_edges+1)
        while to == frm:
            to = random.randrange(nr_edges+1)
        g.add_edge(frm,to)
    
    return g

def con_graf(nr_nodes,nr_edges):
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
    fop.add_vertex(0, random.randrange(2))
    for i in range(1,nr_nodes):
        r = random.choice(list(fop.vert_dict.keys()))
        fop.add_vertex(i, random.randrange(2))
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
        
        
    


    
#gr = graf(4,6)
        
    
    

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a',0)
    g.add_vertex('b',0)
    g.add_vertex('c',1)
    g.add_vertex('d',0)
    g.add_vertex('e',1)
    g.add_vertex('f',0)

    g.add_edge('a', 'b')  
    g.add_edge('a', 'c')
    g.add_edge('a', 'f')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('c', 'd')
    g.add_edge('c', 'f')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')
    g.add_edge('a','b')
    # g.add_vertex(1,1)
    # g.add_vertex(2,0)
    # g.add_edge(1,2)
    
    
    # h = Graph()
    # h.add_edge(1,2)
    # h.add_edge(2,5)
    # h.add_edge(3,4)
    # h.add_edge(4,2)
    # h.add_edge(6,5)
    f = Graph()
    
    f.add_vertex(1,0)
    f.add_vertex(2,1)
    f.add_vertex(3,0)
    f.add_edge(1,2)
    f.add_edge(1,3)
    
    