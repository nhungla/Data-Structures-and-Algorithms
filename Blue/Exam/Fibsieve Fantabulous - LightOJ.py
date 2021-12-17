import math
if __name__ == "__main__":
  tc = int(input())
  for t in range(1, tc + 1):
    n = int(input())
    sq = math.ceil(math.sqrt(n))
    r = sq * sq - n
    x, y = 0, 0
    if r < sq:
      y = r + 1
      x = sq
    else:
      x = 2 * sq - r - 1
      y = sq
    if sq & 1:
      x, y = y, x
    print("Case %s: %s %s" % (t, x, y))