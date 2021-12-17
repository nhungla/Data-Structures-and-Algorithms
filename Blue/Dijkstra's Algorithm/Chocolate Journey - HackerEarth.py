import collections
import heapq
def dijkstra(gr, st, n):
  dists = [float("inf")] * n
  dists[st] = 0
  pool = [(0, st)]
  while pool:
    cur_d, cur = heapq.heappop(pool)
    if cur_d > dists[cur]:
      continue
    for ch, d in gr[cur]:
      if dists[ch] > cur_d + d:
        dists[ch] = cur_d + d
        heapq.heappush(pool, (dists[ch], ch))
  return dists
if __name__ == "__main__":
  n, m, k, x = list(map(int, input().split()))
  cities = list(map(int, input().split()))
  gr = collections.defaultdict(list)
  for _ in range(m):
    u, v, d = list(map(int, input().split()))
    gr[u - 1].append((v - 1, d))
    gr[v - 1].append((u - 1, d))
  A, B = list(map(int, input().split()))
  A_dists = dijkstra(gr, A - 1, n)
  B_dists = dijkstra(gr, B - 1, n)
  ans = float("inf")
  for city in cities:
    if B_dists[city - 1] <= x:
      ans = min(ans, A_dists[city - 1] + B_dists[city - 1])
  print(ans if ans < float("inf") else -1)