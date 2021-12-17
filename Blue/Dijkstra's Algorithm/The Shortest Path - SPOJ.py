import collections
import heapq
def dijkstra(gr, n, st, en):
  dists = [float("inf")] * (n + 1)
  dists[st] = 0
  pool = [(0, st)]
  while pool:
    cur_cost, cur = heapq.heappop(pool)
    if cur_cost > dists[cur]:
      continue
    for ch, cost in gr[cur]:
      if dists[ch] > cur_cost + cost:
        dists[ch] = cur_cost + cost
        heapq.heappush(pool, (dists[ch], ch))
  return dists[en]
if __name__ == "__main__":
  tc = int(input())
  for t in range(tc):
    if t != 0:
      input()
    n = int(input())
    map_idx = {}
    gr = collections.defaultdict(list)
    for idx in range(1, n + 1):
      name = input()
      map_idx[name] = idx
      p = int(input())
      for _ in range(p):
        nr, cost = list(map(int, input().split()))
        gr[idx].append((nr, cost))
    queries = int(input())
    for _ in range(queries):
      st, en = input().split()
      st = map_idx[st]
      en = map_idx[en]
      print(dijkstra(gr, n, st, en))