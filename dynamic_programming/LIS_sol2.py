from sys import stdin
import sys 
sys.setrecursionlimit(10**7)

def longestIncreasingSubsequence(arr, n):
    nex = [0 for j in range(n+1)]

    for i in range(n-1,-1,-1):
        for j in range(i-1,-2,-1):
           take = 0
           if j==-1 or arr[j]<arr[i]:
               take = 1+nex[i+1]
           nonTake = nex[j+1]
       
           nex[j+1] = max(take,nonTake)

    return nex[-1+1]
