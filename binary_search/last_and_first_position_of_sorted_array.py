from os import *
from sys import *
from collections import *
from math import *

def firstAndLastPosition(arr, n, k):
    # Write your code here
    lst = frs = -1
    low = 0
    upr = n-1
    while low<=upr:
        mid = low + (upr-low)//2
        if arr[mid]>=k:
           if arr[mid] == k:
               frs = mid
           upr = mid-1
        else:
           low = mid+1
    
    low = 0
    upr = n-1
    while low<=upr:
        mid = low + (upr-low)//2
        if arr[mid]<=k:
           if arr[mid] == k:
              lst = mid
           low = mid+1
        else:
           upr = mid-1
    
    return frs,lst
            

	
