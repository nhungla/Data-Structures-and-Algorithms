import collections
def dfs(graph, visited, src):
  s = [src]
  visited[src] = True
  while len(s):
    u = s.pop()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        s.append(v)
if __name__ == "__main__":
  testcases = int(input())
  for i in range(testcases):
    person = int(input())
    relats = int(input())
    graph = collections.defaultdict(list)
    for j in range(relats):
      u, v = list(map(int, input().split()))
      graph[u].append(v)
      graph[v].append(u)
    used = [False] * person
    ans = 0
    for u in range(person):
      if used[u]:
        continue
      ans += 1
      dfs(graph, used, u) 
    print(ans)