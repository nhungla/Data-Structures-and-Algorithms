import string
import sys
sys.setrecursionlimit(10000000)
class Node:
    def __init__(self):
        self.count_leaf = 0
        self.child = {}
class Trie:
    def __init__(self):
        self.root = Node()
    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.count_leaf += 1
def suffix_traversal(root, level, start_with):
    cnt = 1
    for c in root.child:
        if level > 0:
            start_with[c] += 1
        cnt += suffix_traversal(root.child[c], level + 1, start_with)     
    return cnt
def prefix_traversal(root, level, suffix_state_count, start_with):
    res = 0
    if level > 0:
        res = suffix_state_count
    for c in root.child:
        if level > 0:
            res -= start_with[c]
        res += prefix_traversal(root.child[c], level + 1, suffix_state_count, start_with)
    return res
if __name__ == '__main__':
    while True:
        p, s = map(int, input().split())
        if p == s == 0:
            break
        suffix_trie = Trie()
        prefix_trie = Trie()
        for i in range(p):
            prefix_trie.add_word(input())

        for i in range(s):
            suffix_trie.add_word(input()[::-1])

        start_with = {c: 0 for c in string.ascii_lowercase}
        suffix_state_count = suffix_traversal(suffix_trie.root, 0, start_with) - 1
        print(prefix_traversal(prefix_trie.root, 0, suffix_state_count, start_with))