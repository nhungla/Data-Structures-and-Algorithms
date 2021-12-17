import collections


def solve(gr, cur, ans):
    ans.add(cur)
    for ne in gr[cur]:
        if ne not in ans:
            solve(gr, ne, ans)


class UniFind:
    def __init__(self, n):
        self.parent = [val for val in range(n + 10)]

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
    n, m = list(map(int, input().split()))
    if n < 3 or n != m:
        print("NO")
        exit()
    gr = []
    graph = collections.defaultdict(list)
    for _ in range(m):
        u, v = list(map(int, input().split()))
        gr.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    """
    uf = UniFind(n)
    for u, v in gr:
      uf.uni(u, v)
  
    ans = True
    for i in range(1, n + 1):
      for j in range(i + 1, n + 1):
        print(uf.find(i), uf.find(j), i, j)
        if uf.find(i) != uf.find(j):
          ans = False
          break
    """
    # print(graph)
    re = set()
    solve(graph, 1, re)
    # print(re)
    print("FHTAGN!" if len(re) == n else "NO")