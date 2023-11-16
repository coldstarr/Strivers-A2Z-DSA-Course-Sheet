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

	def insert(self, root, ele):
		for i in range(31,-1,-1):
			bit = ele>>i & 1
			if not self.containsKey(root,bit):
				root.bits[bit] = Node()
			root = self.get(root,bit)
			
                 
	def getMax(self,root,xi):
		val = 0
		for i in range(31,-1,-1):
			bit = xi>>i & 1
			if root:
				if self.containsKey(root,1-bit):
					root = self.get(root,1-bit)
					val = val | 1<<i
				else:
					root = self.get(root,bit)
			else:
				return -1
		return val

def maxXorQueries(arr, queries):
	# Write your code here.
	trie = Trie()
	root = Node()
	arr.sort()
	q = len(queries)
	out = []
	new_queries = []
	for idx,query in enumerate(queries):
		new_queries.append([idx,*query])
	
	queries = new_queries
	queries.sort(key=lambda x:x[2])

	out = [0]*q
	c = 0
	for query in queries:
		while arr:
			ele = arr.pop(0)
			if ele<=query[2]:
				c+=1
				trie.insert(root,ele)
			else:
				arr = [ele]+arr
				break
		val = trie.getMax(root,query[1])
		if c!=0:
			out[query[0]] = val
		else:
			out[query[0]] = -1
	return out
