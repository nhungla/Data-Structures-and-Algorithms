import collections
if __name__ == "__main__":
  n, m = list(map(int, input().split()))
  arr = list(map(int, input().split()))
  graph = collections.defaultdict(lambda: [])
  for i in range(n - 1):
    u, v = list(map(int, input().split()))
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
  cur_cat = 1 if arr[0] == 1 else 0
  pool = [(cur_cat, 0)]
  set_leaves = {x for x, v in graph.items() if len(v) == 1}
  visited = {0}
  ans = 0
  while pool:
    tmp = []
    for cat, u in pool:
      for v in graph[u]:
        if v in visited:
          continue
        cur_cat = 0 if arr[v] == 0 else (cat + 1)
        if cur_cat > m:
          continue
        if v in set_leaves:
          ans += 1
        tmp.append((cur_cat, v))
        visited.add(v)
    pool = tmp
  print(ans)