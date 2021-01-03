#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:40:11 2021

@author: ironman
"""

def smallestDifference(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxone=0
    idxtwo=0
    current=float('inf')
    smallest=float('inf')
    smallestpair=[]
    while idxone<len(arrayOne) and idxtwo<len(arrayTwo):
        firstnum=arrayOne[idxone]
        secondnum=arrayTwo[idxtwo]
        if firstnum<secondnum:
            current=secondnum-firstnum
            idxone+=1
        elif secondnum<firstnum:
            current=firstnum-secondnum
            idxtwo+=1
        else:
            return [firstnum,secondnum]
        if smallest>current:
            smallest=current
            smallestpair=[firstnum,secondnum]
    return smallestpair

arrayOne=[-1,5,10,20,28,3]
arrayTwo=[26,124,134,135,15,17]
ans=smallestDifference(arrayOne, arrayTwo)
print(ans)
            