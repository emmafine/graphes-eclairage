# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:17:20 2020

@author: Asus
"""

class Vertex:
    def __init__(self, node):
        self.id = node
        self.light = 1
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
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

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

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
            for neighbour in self.vert_dict[node].adjacent.keys():
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
    
    # def opti_lit(self):
    #     ok = 1
    #     if self.is_lit() == 0:
    #         return 0
    #     for node in self.vert_dict.keys():
    #         if self.vert_dict[node].light == 1:
    #             self.vert_dict[node] = 0
    #             if self.is_lit() == 1:
    #                 ok = 0
    #             self.vert_dict[node].light = 1
    #     if ok == 1:
    #         return 1
    #     else:
    #         return 0
    
    def is_opti_lit(self):
        ok = 1
        if self.is_lit() == 0:
            return 0
        for node in self.vert_dict.keys():
            if self.vert_dict[node].light == 1:
                self.vert_dict[node].light = 0
                if self.is_lit() == 1:
                    ok = 0
        if ok == 0:
            return 0
        else:
            return 1
        
            
        
    
    
        
    
    

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