from os import *
from sys import *
from collections import *
from math import *


def matrixMultiplication(arr, n):
	# Write your code here.
	dp = [[0 for j in range(n)] for i in range(n)]
	for i in range(n):
		dp[i][i] = 0	
	for i in range(n-1,0,-1):
		for j in range(i+1,n):
			min_mul = float('inf') 
			for k in range(i,j):
			   min_mul = min(min_mul, arr[i-1]*arr[k]*arr[j]+dp[i][k]+dp[k+1][j])
			dp[i][j] = min_mul
	out = dp[1][n-1]
	return out
