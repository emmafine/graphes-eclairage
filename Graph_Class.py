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

    
    # def swtich_on(self):
    #     self.light = 1
        
    # def switch_off(self):
    #     self.light = 1

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.edges = []
        

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
        self.edges.append({frm,to})

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
    
    def is_lit_nodes(self):
        lit_dict = self.lit_dict()
        if 0 in lit_dict.values():
            return 0
        else:
            return 1
        
    def switch_on(self,i):
        self.vert_dict[i].light = 1
        
    def switch_off(self,i):
        self.vert_dict[i].light = 0
    
    
    def is_opti_lit_nodes(self):
        ok = 1
        if self.is_lit() == 0:
            return 0
        
        #check is the leaves are lit -> they can be always off
        #in a minimally lit graph
        
        for node in self.vert_dict.keys():
            if len(self.vert_dict[node].adjacent) == 1:
                if self.vert_dict[node].light == 1:
                    ok = 0
                    
        #check if it's optimally lit
                    
        for node in self.vert_dict.keys():
            if self.vert_dict[node].light == 1:
                self.vert_dict[node].light = 0
                if self.is_lit() == 1:
                    ok = 0
                self.vert_dict[node].light = 1
        if ok == 0:
            return 0
        else:
            return 1
    
    
    def is_lit(self):
        #checks if every street is enlightened
        ok = 1
        for edge in self.edges:
            l = list(edge)
            
            if self.vert_dict[l[0]].light == 0 and self.vert_dict[l[1]].light == 0:
                ok = 0
        return ok
    
    def is_min_lit(self):
        #enlever un lampadaire plonge au moins une rue dans l'obscurite
        if self.is_lit() == 0:
            return 0

        for node in self.vert_dict.keys():
            if self.vert_dict[node].light == 1:
                self.switch_off(node)
                if self.is_lit() == 1:
                    return 0
                self.switch_on(node)
        return 1
    
    def switch_graph_on(self):
        for i in self.vert_dict.keys():
            self.vert_dict[i].light = 1
                
                
    
    


##############################################Class Ends
    
  


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


    f = Graph()
    
    f.add_vertex(1,0)
    f.add_vertex(2,1)
    f.add_vertex(3,0)
    f.add_vertex(4,0)
    f.add_vertex(5,1)
    f.add_vertex(6,1)
    f.add_vertex(7,1)
    
    f.add_edge(1, 2)
    f.add_edge(2, 3)
    f.add_edge(4, 2)
    f.add_edge(4, 5)
    f.add_edge(4, 6)
    f.add_edge(5, 6)
    f.add_edge(6, 7)
    f.add_edge(4, 7)