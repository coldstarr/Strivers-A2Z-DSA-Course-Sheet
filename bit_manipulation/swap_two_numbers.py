def swapNumber(a:int,  b: int) -> None:
    # write your code here
    a = a^b
    b = b^a
    a = a^b
    return a,b
