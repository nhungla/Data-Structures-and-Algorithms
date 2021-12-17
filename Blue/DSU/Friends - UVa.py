class UniFind:
  def __init__(self, n):
    self.parents = [i for i in range(n + 1)]
    #self.ranks = [i for i in range(n + 1)]
    self.count = [1] * (n + 1)
  def find(self, x):
    if x != self.parents[x]:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]
  def uni(self, x, y):
    rx, ry = self.find(x), self.find(y)
    if rx == ry:
      return False
    if self.count[rx] > self.count[ry]:
      self.count[rx] += self.count[ry]
      self.parents[ry] = rx
    else:
      self.count[ry] += self.count[rx]
      self.parents[rx] = ry
    return True
if __name__ == "__main__":
  tcs = int(input())
  for _ in range(tcs):
    n, m = list(map(int, input().split()))
    uf = UniFind(n)
    for _ in range(m):
      u, v = list(map(int, input().split()))
      uf.uni(u, v)
    ans = 0
    for val in uf.count:
      ans = max(ans, val)
    print(ans)