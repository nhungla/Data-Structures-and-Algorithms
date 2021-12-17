import collections
import heapq
if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    p = int(input())
    n = int(input())
    m = int(input())
    gr = collections.defaultdict(list)
    for _ in range(m):
      a, b, c = list(map(int, input().split()))
      gr[a - 1].append((b - 1, c))
      gr[b - 1].append((a - 1, c))
    costs = [float("inf")] * n
    costs[0] = 0
    visited = [False] * n
    pool = [(0, 0)]
    while pool:
      cur_cost, cur = heapq.heappop(pool)
      visited[cur] = True
      for ch, d in gr[cur]:
        if visited[ch]:
          continue
        if costs[ch] > d * p:
          costs[ch] = d * p
          heapq.heappush(pool, (costs[ch], ch))
    print(sum(costs))