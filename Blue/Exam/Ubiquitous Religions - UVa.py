class UniFind:
    def __init__(self, n):
        self.parent = list(range(n + 10))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def uni(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        self.parent[rx] = ry
        return True


if __name__ == "__main__":
    tc = 1
    while True:
        n, m = list(map(int, input().split()))
        if n == m == 0:
            break
        uf = UniFind(n)
        ans = 0
        for _ in range(m):
            x, y = list(map(int, input().split()))
            uf.uni(x, y)
        for i in range(1, n + 1):
            if i == uf.parent[i]:
                ans += 1
        print("Case %s: %s" % (tc, ans))
        tc += 1
