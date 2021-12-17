import collections
import heapq
def find_min_decibel(gr, st, n, path, dists):
  pool = [(0, st)]
  visited = [False] * n
  dists[st] = 0
  while pool:
    d, u = heapq.heappop(pool)
    visited[u] = True
    for ch, dec in gr[u]:
      if visited[ch]:
        continue
      if dists[ch] > dec:
        dists[ch] = dec
        heapq.heappush(pool, (dec, ch))
        path[ch] = u
if __name__ == "__main__":
  tc = 0
  while True:
    n, s, q = list(map(int, input().split()))
    if n == s == q == 0:
      break
    if tc != 0:
      print()
    tc += 1
    gr = collections.defaultdict(list)
    for _ in range(s):
      u, v, d = list(map(int, input().split()))
      gr[u - 1].append((v - 1, d))
      gr[v - 1].append((u - 1, d))
    print("Case #%s" % tc)
    path = [[-1] * n for _ in range(n)]
    dists = [[float("inf")] * n for _ in range(n)]
    found = [False] * n
    for _ in range(q):
      st, en = list(map(int, input().split()))
      st, en = st - 1, en - 1
      if not found[st]:
        find_min_decibel(gr, st, n, path[st], dists[st])
        found[st] = True
      ans = float("-inf")
      while en != st:
        if path[st][en] == -1:
          ans = -1
          break
        ans = max(ans, dists[st][en])
        en = path[st][en]
      print(ans if ans != -1 else "no path")