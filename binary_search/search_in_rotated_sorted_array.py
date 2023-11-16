from os import *
from sys import *
from collections import *
from math import *

def binarySearch(low,upr,arr,n,k):
	while low<=upr:
	   mid = low+(upr-low)//2
	   if arr[mid] == k:
	      return mid
	   elif arr[low]<=arr[mid]:
		   if arr[low]<=k<=arr[mid]:
			   upr = mid-1
		   else:
	   		   low = mid+1
	   else:
		   if arr[mid]<=k<=arr[upr]:
		   	  low = mid+1
		   else:
			   upr = mid-1
	return -1

def search(arr, n, k):
	out = binarySearch(0,n-1,arr,n,k)
	return out
