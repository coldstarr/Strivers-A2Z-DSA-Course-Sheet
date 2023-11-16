from sys import stdin
import sys 
sys.setrecursionlimit(10**7)

def lower_bound(ele,lis,c):
    l,r = 0,c
    res = 0
    while l<=r:
        mid = (l+r)//2
        if lis[mid]>=ele:
            res=mid
            r = mid-1
        elif lis[mid]<ele:
            l = mid+1
    return res

def longestIncreasingSubsequence(arr, n):
    lis = [arr[0]]
    c=1
    if n==1:
       return c
    for ele in arr[1:]:
        if ele>lis[-1]:
            lis.append(ele)
            c+=1
        else:
            idx = lower_bound(ele,lis,c)
            lis[idx] = ele
    return c
    
    































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
