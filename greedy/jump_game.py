from typing import List

def jump_search(jump: List[int], n: int) -> bool:
    # write your code here
    if not jump[0]:
        return False
    last_idx = n-1
    flag = False
    for i in range(n-2,-1,-1):
        if jump[i]:
            if jump[i]>=(last_idx-i):
               last_idx = i
               flag = True
            else:
                return False
    return flag
        
