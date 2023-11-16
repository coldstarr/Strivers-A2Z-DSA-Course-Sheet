from typing import *

def searchInARotatedSortedArrayII(arr : List[int], k : int) -> bool:
    n = len(arr)
    low = 0
    upr = n-1
    # Write your code here.
    while low<=upr:
        mid = low+(upr-low)//2
        if arr[mid] == k:
           return True
        elif arr[low]==arr[mid]==arr[upr]:
            low = low+1
            upr = upr-1
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
    return False
