import collections
class UniFind:
  def __init__(self, n):
    self.parents = [val for val in range(n + 10)]
  def find(self, x):
    if self.parents[x] != x:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]
  def uni(self, x, y):
    rx, ry = self.find(x), self.find(y)
    if rx == ry:
      return False
    self.parents[rx] = ry
    return True
if __name__ == "__main__":
  n, a, b = list(map(int, input().split()))
  mp = collections.defaultdict(lambda: 0)
  arr = [0] + list(map(int, input().split()))
  uf = UniFind(n)
  for idx, val in enumerate(arr[1:], 1):
    mp[val] = idx
  for i in range(1, n + 1):
    if mp[a - arr[i]]:
      tmp = uf.uni(i, mp[a - arr[i]])
    else:
      tmp = uf.uni(i, n + 2)
    if mp[b - arr[i]]:
      tmp = uf.uni(i, mp[b - arr[i]])
    else:
      tmp = uf.uni(i, n + 1)
  if uf.find(n + 1) == uf.find(n + 2):
    print("NO")
  else:
    print("YES")
    ans = []
    for i in range(1, n + 1):
      ans.append("0") if uf.find(n + 1) == uf.find(i) else ans.append("1")
    print(" ".join(ans))