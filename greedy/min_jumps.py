from os import *
from sys import *
from collections import *
from math import *

def minJumps(arr):
    if arr[0]==0:
        return -1
    n = len(arr)
    cur = arr[0]
    cur_idx = 0
    max_jump = arr[0]
    c = 1
    for i in range(1,n-1):
        if (i-cur_idx)>cur:
           c+=1
           cur = max_jump
        if arr[i]+i>max_jump:
           max_jump = arr[i]+i
           cur_idx = i
    
    if arr[cur_idx]+cur_idx>=(n-1-cur_idx):
        return c
    return -1

        
    
    

