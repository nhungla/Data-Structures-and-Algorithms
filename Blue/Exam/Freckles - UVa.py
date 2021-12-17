import heapq
import math
import collections
def find_dis(a, b):
  xa, ya = a
  xb, yb = b
  return math.sqrt((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb))
def helper(points, n):
  visited = [False] * n
  dists = [float("inf")] * n
  dists[0] = 0
  pool = [(0, 0)]
  while pool:
    cur_dist, cur = heapq.heappop(pool)
    visited[cur] = True
    for ch, dist in gr[cur]:
      if visited[ch]:
        continue
      if dists[ch] > dist:
        dists[ch] = dist
        heapq.heappush(pool, (dist, ch))
  return sum(dists)
if __name__ == "__main__":
  tcs = int(input())
  for _ in range(tcs):
    input()
    n = int(input())
    points = []
    gr = collections.defaultdict(list)
    for _ in range(n):
      x, y = list(map(float, input().split()))
      points.append((x, y))
    for i in range(n):
      for j in range(i + 1, n):
        d = find_dis(points[i], points[j])
        gr[i].append((j, d))
        gr[j].append((i, d))
    ans = helper(points, n)
    print(format(ans, ".2f"))
    print()