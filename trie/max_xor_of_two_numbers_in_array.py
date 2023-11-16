from os import *
from sys import *
from collections import *
from math import *

from typing import *

class Node:
    def __init__(self):
        self.bits = [None,None]
                
class Trie:
    def containsKey(self,root,bit):
        return root.bits[bit]!=None

    def get(self,root,bit):
        return root.bits[bit]

    def insert(self, root, ar):
        base_root = root
        for ele in ar:
            root = base_root
            for i in range(31,-1,-1):
                bit = ele>>i & 1
                if not self.containsKey(root,bit):
                    root.bits[bit] = Node()
                root = self.get(root,bit)
                 
    def getMax(self,root,ar):
        mx = 0
        base_root = root
        for ele in ar:
            val = 0
            root = base_root
            for i in range(31,-1,-1):
                bit = ele>>i & 1
                if self.containsKey(root,1-bit):
                    root = self.get(root,1-bit)
                    val = val | 1<<i
                else:
                    root = self.get(root,bit)
            mx = max(val,mx)
        return mx

def maximumXor(A: List[int]) -> int:
    # Write your code here.
    trie = Trie()
    root = Node()
    trie.insert(root, A)
    return trie.getMax(root, A)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        a = [int(j) for j in input().split()]
        print(maximumXor(a))
