IS_LEAF = "is_leaf"


class Trie:
    def __init__(self):
        self.root = {}

    def __repr__(self):
        return "%s" % (self.root)

    def add_num(self, num):
        r = self.root
        for n in num:
            r = r.setdefault(n, {})
        r[IS_LEAF] = True

    def _traverse(self, node):
        if node == None:
            return True
        if node.get(IS_LEAF):
            return False if len(node) > 1 else True
        ans = True
        for ch in node:
            ans &= self._traverse(node[ch])
        return ans

    def traverse(self):
        return self._traverse(self.root)


if __name__ == "__main__":
    tc = int(input())
    for t in range(1, tc + 1):
        n = int(input())
        tree = Trie()
        for _ in range(n):
            tree.add_num(input())
        ans = tree.traverse()
        ss = "YES" if ans else "NO"
        print("Case %s: %s" % (t, ss))
