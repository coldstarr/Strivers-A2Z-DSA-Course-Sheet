from os import *
from sys import *
from collections import *
from math import *

def shortestSupersequence(a: str, b: str) -> str:
	# Write your code here.
    n = len(a)
    m = len(b)
    
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
       for j in range(1,m+1):
    	   dropS = dropT = dropB = 0
    	   if a[i-1]==b[j-1]:
    	   	dropB = 1+dp[i-1][j-1]
    	   else:
    	   	dropS = dp[i-1][j]
    	   	dropT = dp[i][j-1]
    	   dp[i][j] = max(dropB,dropS,dropT)
    
    i = n
    j = m
    st = ''
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
           st=a[i-1]+st
           i-=1
           j-=1
        else:
            if dp[i][j-1]<dp[i-1][j]:
                st=a[i-1]+st
                i-=1
            else:
                st=b[j-1]+st
                j-=1
    while i>0:
        st = a[i-1]+st
        i-=1
    
    while j>0:
        st = b[j-1]+st
        j-=1

    return st
