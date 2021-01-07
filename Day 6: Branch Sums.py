#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:29:25 2021

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
        
def BranchSum(root):
    sum=[]
    CalculateBranchSum(root,0,sum)
    return sum

def CalculateBranchSum(node,runningSum,sum):
    if node is None:
        return
    newRunningSum=runningSum+node.value
    if node.left is None and node.right is None:
        sum.append(newRunningSum)
        return
    CalculateBranchSum(node.left, newRunningSum, sum)
    CalculateBranchSum(node.right, newRunningSum, sum)
    
tree=BST(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(5)
tree.insert(1)

ans=BranchSum(tree)
print(ans)