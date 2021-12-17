class Node:
    def __init__(self, val):
        self.child = {}
        self.is_blocked = False
        self.val = val


class Trie:
    def __init__(self):
        self.root = Node('')

    def add(self, length, id, res):
        st = [self.root]
        while length and len(st):
            u = st[-1]
            length -= 1
            if 0 not in u.child:
                u.child[0] = Node('0')
            if not u.child[0].is_blocked:
                st.append(u.child[0])
            else:
                if 1 not in u.child:
                    u.child[1] = Node('1')
                if not u.child[1].is_blocked:
                    st.append(u.child[1])
                else:
                    u.is_blocked = True
                    length += 2
                    st.pop()
            if length == 0:
                st[-1].is_blocked = True
                res[id] = ''.join(node.val for node in st)
                return True
        return False


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted([(a[i], i) for i in range(n)])

    trie = Trie()
    res = [None] * n
    ans = True
    for length, i in a:
        if not trie.add(length, i, res):
            print('NO')
            ans = False
    if ans:
        print('YES')
        for length in res:
            print(length)