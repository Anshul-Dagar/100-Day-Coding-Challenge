#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:30:49 2021

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



def findClosestValueInBst(target,tree):
    return findClosestValueInBstHelper(target,tree,float("inf"))

def findClosestValueInBstHelper(target,tree,closest):
    currentnode=tree
    while currentnode is not None:
        if abs(target-closest)>abs(target-currentnode.value):
            closest=currentnode.value
        if target>currentnode.value:
            currentnode=currentnode.right
        elif target<currentnode.value:
            currentnode=currentnode.left
        else:
            break
    return closest

tree=BST(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(5)
tree.insert(1)

ans=findClosestValueInBst(9,tree)
print(ans)