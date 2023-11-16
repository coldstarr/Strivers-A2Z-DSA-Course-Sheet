from sys import stdin
import sys 
sys.setrecursionlimit(10**7)

def longestIncreasingSubsequence(arr, n) :
    dp = [1 for i in range(n)]
    trace = [i for i in range(n)]
    mx = 1
    last_idx = 0
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and dp[j]+1>dp[i]:
              dp[i] = dp[j]+1
              trace[i] = j
        if dp[i]>mx:
            mx = dp[i]
            last_idx = i
    
    ls = [0]*mx
    ls[0] = arr[last_idx]
    ind = 1
    while trace[last_idx]!=last_idx:
        last_idx = trace[last_idx]
        ls[ind] = arr[last_idx]
        ind+=1
    return list(reversed(ls))
    
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
