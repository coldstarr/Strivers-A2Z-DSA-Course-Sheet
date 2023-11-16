#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import *
from sys import *
from collections import *
from math import *


class Node:

    def __init__(self):
        self.alpha = [0 for i in range(26)]
        self.end = False


class Trie:

    def __init__(self):
        self.ord = {}

    def containsKey(self, ch, root):
        if not root.alpha[self.ord[ch]]:
            return False
        return True
    
    def put(self, ch, root, node):
        root.alpha[self.ord[ch]] = node

    def get(self, ch, root):
        return root.alpha[self.ord[ch]]
    
    def setEnd(self,node):
        node.end = True
    
    def getEnd(self,node):
        return node.end

    def insert(
        self,
        word,
        n,
        root,
        ):
        for (idx, ch) in enumerate(word):
            alpha = self.ord[ch]
            if not self.containsKey(ch, root):
                self.put(ch,root,Node())
            root = self.get(ch,root)
        self.setEnd(root)
        

    def search(
        self,
        word,
        n,
        root,
        ):
        for (idx, ch) in enumerate(word):
            alpha = self.ord[ch]

            if not self.containsKey(ch, root):
                return 'FALSE'
            root = self.get(ch,root)
        return self.getEnd(root)


if __name__ == '__main__':
    trie = Trie()
    for (idx, alpha_asci) in enumerate(range(97, 123)):
        trie.ord[chr(alpha_asci)] = idx
    root = Node()
    n = int(input())
    for i in range(n):
        (op, *word) = input().split()
        if len(word) ==1:
            word = word[0]
            lg = len(word)

            if op == '1':
                if lg >= 1 and lg <= 20 and word.isalpha() and word.islower():
                    trie.insert(word, lg, root)
            else:
                if lg >= 1 and lg <= 20 and word.isalpha() and word.islower():
                  print(trie.search(word, len(word), root))
                else:
                  print('FALSE')
