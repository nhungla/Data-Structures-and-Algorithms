class UniFind:
  def __init__(self, n):
    self.parent = list(range(2 * n + 10))
    self.rank = [1] * (2 * n + 10)
  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
  def uni(self, x, y):
    rx, ry = self.find(x), self.find(y)
    if rx == ry:
      return False
    if self.rank[rx] > self.rank[ry]:
      self.parent[ry] = rx
      self.rank[rx] += self.rank[ry]
    else:
      self.parent[rx] = ry
      self.rank[ry] += self.rank[rx]
    return True
if __name__ == "__main__":
  n = int(input())
  uf = UniFind(n)
  while True:
    c, x, y = list(map(int, input().split()))
    if c == x == y == 0:
      break
    if c == 1:
      if uf.find(x) == uf.find(y + n) or uf.find(x + n) == uf.find(y):
        print("-1")
      else:
        uf.uni(x, y)
        uf.uni(x + n, y + n)
    elif c == 2:
      if uf.find(x) == uf.find(y) or uf.find(x + n) == uf.find(y + n):
        print("-1")
      else:
        uf.uni(x, y + n)
        uf.uni(y, x + n)
    elif c == 3:
      if uf.find(x) == uf.find(y) or uf.find(x + n) == uf.find(y + n):
        print("1")
      else:
        print("0")
    elif c == 4:
      if uf.find(x) == uf.find(y + n) or uf.find(x + n) == uf.find(y):
        print("1")
      else:
        print("0")