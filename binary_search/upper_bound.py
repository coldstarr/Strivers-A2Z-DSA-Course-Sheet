def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    low = 0
    upr = n-1

    lwr_bound = n
    while low<=upr:
       mid = low+(upr-low)//2
       if x<arr[mid]:
           lwr_bound = mid
           upr = mid-1
       else:
           low = mid+1
    return lwr_bound
