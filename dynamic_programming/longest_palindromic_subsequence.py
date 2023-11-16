from os import *
from sys import *
from collections import *
from math import *

def longestPalindromeSubsequence(s):
    t = ''.join(reversed(s))
    n = len(s)
    m = n
    if n==0 or m == 0:
    	return 0
    cur = [0 for j in range(m+1)]
    prev = [0 for j in range(m+1)]  
    for i in range(1,n+1):
       for j in range(1,m+1):
    	   dropS = dropT = dropB = 0
    	   if s[i-1]==t[j-1]:
    	   	dropB = 1+prev[j-1]
    	   else:
    	   	dropS = prev[j]
    	   	dropT = cur[j-1]
    	   cur[j] = max(dropB,dropS,dropT)
       prev = cur
       cur = [0 for j in range(m+1)]    
    out = prev[m]
    return out
