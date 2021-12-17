class Node:
    def __init__(self, count=0):
        self.child = {}
        self.count = count


class Trie:
    def __init__(self):
        self.root = Node()

    def add_name(self, word):
        r = self.root
        for w in word:
            if w not in r.child:
                r.child[w] = Node()
            r = r.child[w]
            r.count += 1

    def find(self, word):
        r = self.root
        for w in word:
            if w not in r.child:
                return 0
            r = r.child[w]
        return r.count


if __name__ == "__main__":
    n = int(input())
    tree = Trie()
    for _ in range(n):
        key, val = input().split()
        if key == "add":
            tree.add_name(val)
        elif key == "find":
            ans = tree.find(val)
            print(ans)