from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(input) :
    # Write your code here.
    char = dict()
    l = 0
    r = 0
    max_len = 0
    for idx,ch in enumerate(input):
        if ch in char and l<=char[ch]:
           l = char[ch]+1
        char[ch] = idx
        max_len = max(r-l+1,max_len)
        r+=1
    return max_len
