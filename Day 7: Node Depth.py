#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:44:10 2021

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
    
def nodeDepth(self,depth=0):
    root=self
    if root is None:
        return 0
    return depth + nodeDepth(root.left,depth+1) + nodeDepth(root.right,depth+1)
    
tree=BST(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(5)
tree.insert(1)

ans=nodeDepth(tree,depth=0)
print(ans)