class UniFind:
  def __init__(self, n):
    self.parent = list(range(n + 10))
  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
  def uni(self, x, y):
    rx, ry = self.find(x), self.find(y)
    if ry == rx:
      return False
    self.parent[rx] = ry
    return True
if __name__ == "__main__":
  n = int(input())
  points = []
  for _ in range(n):
    points.append(list(map(int, input().split())))
  if n == 1:
    print(0)
    exit()
  uf = UniFind(n)
  for i in range(n - 1):
    x1, y1 = points[i]
    for j in range(i + 1, n):
      x2, y2 = points[j]
      if x1 == x2 or y1 == y2:
        uf.uni(i, j)
  ans = set()
  for i in range(n):
    ans.add(uf.find(i))
  print(len(ans) - 1)