from typing import *

def bitManipulation(num : int, i : int) -> List[int]:
    # Write your code here.
    i=i-1
    get = (num&(1<<i))>>i
    bset = num|1<<i
    clr = (num|1<<i)-(1<<i)
    return get,bset,clr
