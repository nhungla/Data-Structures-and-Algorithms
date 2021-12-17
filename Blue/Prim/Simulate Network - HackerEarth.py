import collections
import heapq
def helper(gr, n):
  dists = [float("inf")] * n
  dists[0] = 0
  visited = [False] * n
  pool = [(0, 0)]
  while pool:
    curl, cur = heapq.heappop(pool)
    visited[cur] = True
    for ch, l in gr[cur]:
      if visited[ch]:
        continue
      if dists[ch] > l:
        dists[ch] = l
        heapq.heappush(pool, (l, ch))
  return dists
if __name__ == "__main__":
  n, m = list(map(int, input().split()))
  gr = collections.defaultdict(list)
  for _ in range(m):
    a, b, l = list(map(int, input().split()))
    gr[a - 1].append((b - 1, l))
    gr[b - 1].append((a - 1, l))
  q = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  cur_idx = 0
  dists = helper(gr, n)
  dists.sort(key=lambda x: -x)
  for i in range(n):
    if cur_idx >= q:
      break
    if dists[i] > arr[cur_idx]:
      dists[i] = arr[cur_idx]
      cur_idx += 1
  print(sum(dists))