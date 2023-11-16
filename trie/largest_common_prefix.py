import sys


class Node:
    def __init__(self):
        self.alpha = [0] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.ord = {}

    def containsKey(self, ch, root):
        return bool(root.alpha[self.ord[ch]])

    def put(self, ch, root, node):
        root.alpha[self.ord[ch]] = node

    def get(self, ch, root):
        return root.alpha[self.ord[ch]]

    def setEnd(self, node):
        node.end = True

    def getEnd(self, node):
        return node.end

    def insert(self, word, root):
        for ch in word:
            alpha = self.ord[ch]
            if not self.containsKey(ch, root):
                self.put(ch, root, Node())
            root = self.get(ch, root)
        self.setEnd(root)

    def char_count(self, root):
        return sum(ch != 0 for ch in root.alpha)

    def find_prefix(self, word, root):
        prefix = ""
        for ch in word:
            if self.char_count(root) == 1:
                prefix += ch
            else:
                return prefix
            root = self.get(ch, root)
        return prefix


def longestCommonPrefix(arr, n):
    trie = Trie()
    for idx, alpha_asci in enumerate(range(97, 123)):
        trie.ord[chr(alpha_asci)] = idx
    root = Node()

    minlen_word = 1001
    word = ""
    for wrd in arr:
        lg = len(wrd)
        if lg < minlen_word:
            minlen_word = lg
            word = wrd
        trie.insert(wrd, root)

    return trie.find_prefix(word, root)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for _ in range(n):
        m = int(sys.stdin.readline())
        words = sys.stdin.readline().split()
        print(longestCommonPrefix(words, m))
