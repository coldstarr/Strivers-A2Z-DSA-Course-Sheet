from sys import stdin
import sys 
sys.setrecursionlimit(10**7)

def longestIncreasingSubsequence(arr, n) :
    dp = [[0 for j in range(n+1)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        for j in range(i-1,-2,-1):
            take = nonTake = 0
            if j==-1 or arr[j]<arr[i]:
                take = 1+dp[i+1][i+1]
            nonTake = dp[i+1][j+1]
            dp[i][j+1] = max(take,nonTake)
    return dp[0][-1+1]
  
#taking inpit using fast I/O
def takeInput() :
    n = int(input())

    if n==0 :
        return list(), n
        
    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(longestIncreasingSubsequence(arr, n))
