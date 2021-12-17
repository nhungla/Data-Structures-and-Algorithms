IS_LEAF = "is_leaf"


class Trie:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        r = self.root
        for w in word:
            r = r.setdefault(w, {})
            if r.get(IS_LEAF):
                return True
        r[IS_LEAF] = True
        return False


if __name__ == "__main__":
    tcs = int(input())
    for _ in range(tcs):
        n = int(input())
        ans = True
        tree = Trie()
        words = []
        for i in range(n):
            word = input()
            words.append(word)
        words.sort()
        for word in words:
            if tree.add_word(word):
                ans = False
                break
        print("YES" if ans else "NO")
