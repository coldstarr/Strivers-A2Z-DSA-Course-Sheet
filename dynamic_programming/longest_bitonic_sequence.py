from os import *
from sys import *
from collections import *
from math import *

def longestIncreasingSubsequence(arr, n) :
    dp = [1 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and dp[j]+1>dp[i]:
              dp[i] = dp[j]+1
    return dp

def longestBitonicSequence(arr, n):
    # Write your code here.
    dp1 = longestIncreasingSubsequence(arr,n)
    rev_arr = list(reversed(arr))
    dp2 = longestIncreasingSubsequence(rev_arr,n)
    mx = 0
    dp2.reverse()
    for ele1,ele2 in zip(dp1,dp2):
        mx = max(mx, ele1+ele2)
    return mx-1
