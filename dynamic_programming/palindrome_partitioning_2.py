from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
import sys
setrecursionlimit(10**6)

def ispalindrome(i,j,string):
    p1 = i
    p2 = j
    while p1<p2:
       if string[p1] == string[p2]:
           p1+=1
           p2-=1
       else:
           return False
    return True

def palindromePartitioning(string):
    # Write your code here.
    n = len(string)
    dp = [0 for i in range(n+1)]
    for i in range(n-1,-1,-1):
       cost = n
       for j in range(i,n):
           if ispalindrome(i,j,string):
             cost = min(cost, 1+dp[j+1])
       dp[i] = cost
    out = dp[0]
    return out-1

# Main
t = int(input())
while t:
    string = list(map(str, input()))
    while(" " in string):
        string.remove(" ")
    print(palindromePartitioning(string))
    t = t-1
