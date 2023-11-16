def findPeakElement(arr: [int]):
    # Write your code here
    n = len(arr)
    
    if n == 2:
       return arr.index(max(arr))
      
    low = 0
    upr = n-1

    while low<=upr:
       mid = low+(upr-low)//2
       if (mid==0 and arr[mid]>arr[mid+1]) or (mid==n-1 and arr[mid]>arr[mid-1]):
          return mid
       if arr[mid-1]<arr[mid]>arr[mid+1]:
          return mid
       elif arr[mid-1]<arr[mid]:
          low = mid+1
       else:
          upr = mid
