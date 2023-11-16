from os import *
from sys import *
from collections import *
from math import *

from typing import List


def maxCoins(a: List[int]) -> int:
	# Write your code here.
    n = len(a)
    a = [1]+a+[1]
    dp = [[0 for j in range(n+2)] for i in range(n+2)]
    
    for i in range(n,0,-1):
        for j in range(i,n+1):
           mx = 0
           for k in range(i,j+1):
               mx = max(mx, a[i-1]*a[k]*a[j+1]+dp[i][k-1]+dp[k+1][j])
           dp[i][j] = mx
    out = dp[1][n]
    return out
