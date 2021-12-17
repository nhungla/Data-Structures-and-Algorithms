class Node:
    def __init__(self):
        self.child = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.tree = Node()
        self.total = 0

    def add_word(self, word):
        r = self.tree
        for idx, w in enumerate(word):
            level = idx + 1
            if w not in r.child:
                r.child[w] = Node()
            r = r.child[w]
            r.count += 1
            self.total = max(self.total, r.count * level)


if __name__ == "__main__":
    tc = int(input())
    for t in range(tc):
        n = int(input())
        tree = Trie()
        for _ in range(n):
            word = input()
            tree.add_word(word)
        print("Case %s: %s" % (t + 1, tree.total))
