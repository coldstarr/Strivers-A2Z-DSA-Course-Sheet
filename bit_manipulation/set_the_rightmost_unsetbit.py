from typing import *

def setBits(N : int) -> int:
    # Write your code here.
    val = (N^(N+1))
    return N if val>N else N|val
