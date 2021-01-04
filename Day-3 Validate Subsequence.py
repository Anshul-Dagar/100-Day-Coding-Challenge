#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:24:53 2021

@author: ironman
"""

def validate_subsequence(array,sequence):
    arrayidx=0
    sequenceidx=0
    while arrayidx<len(array) and sequenceidx<len(sequence):
        if(array[arrayidx] == sequence[sequenceidx]):
            sequenceidx+=1
        arrayidx+=1
    return sequenceidx==len(sequence)

array=[5,1,22,25,6,-1,10]
sequence=[1,6,-1,10]
ans=validate_subsequence(array, sequence)
print(ans)