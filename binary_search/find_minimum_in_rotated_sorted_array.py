def findMin(arr: [int]):
    # Write your code here.
    n = len(arr)
    low = 0
    upr = n-1
    min_ele = float('inf')
    while low<=upr:
       mid = low+(upr-low)//2
       
       if arr[low]<=arr[mid]:
          min_ele = min(min_ele,arr[low])
          low = mid+1
       else:
          min_ele = min(min_ele,arr[mid])
          upr = mid-1

    return min_ele
