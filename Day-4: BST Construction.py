#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:47:31 2021

@author: ironman
"""

class BST:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
    def insert(self,value):
        currentnode=self
        while True:
            if value<currentnode.value:
                if currentnode.left is None:
                    currentnode.left=BST(value)
                    break
                else:
                    currentnode=currentnode.left
            else:
                if currentnode.right is None:
                    currentnode.right=BST(value)
                    break
                else:
                    currentnode=currentnode.right
        return self
    
    def contain(self,value):
        currentnode=self
        while currentnode is not None:
            if value<currentnode.value:
                currentnode=currentnode.left
            elif value>currentnode.value:
                currentnode=currentnode.right
            else:
                return True
        return False

tree=BST(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(5)
tree.insert(1)

ans=tree.contain(1)

print(ans)
                