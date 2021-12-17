import collections
def bfs(graph, s, n):
  arr = [-1] * n
  q = [s]
  visited = {s}
  count = 0
  while q:
    count += 1
    tmp = []
    for u in q:
      for ch in graph[u]:
        if ch in visited:
          continue
        tmp.append(ch)
        visited.add(ch)
        arr[ch] = count * 6
    q = tmp
  return [val for idx, val in enumerate(arr) if idx != s]
if __name__ == "__main__":
  q = int(input())
  for i in range(q):
    n, m = list(map(int, input().split()))
    graph = collections.defaultdict(list)
    for j in range(m):
      u, v = list(map(int, input().split()))
      graph[u - 1].append(v - 1)
      graph[v - 1].append(u - 1)
    start = int(input())
    ans = bfs(graph, start - 1, n)
    print(' '.join(map(str,ans)))