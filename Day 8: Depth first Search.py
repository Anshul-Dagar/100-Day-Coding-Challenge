#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:03:03 2021

@author: ironman
"""

class Node:
    def __init__(self,name):
        self.children=[]
        self.name=name
        
    def add(self,name):
        self.children.append(Node(name))
        
    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

graph=Node('A')
graph.add('B')
graph.add('C')
graph.add('D')
graph.add('E')
graph.add('F')
graph.add('G')
graph.add('H')

array=[]
print(Node.depthFirstSearch(graph,array))


        