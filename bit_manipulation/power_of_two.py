def isPowerOfTwo(n:int) -> bool:
    # Write your code here
    
    if n&(n-1):
        return False
    return True
