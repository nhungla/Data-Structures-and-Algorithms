def floyd_warshall(graph, max_end):
  for k in range(max_end):
    for i in range(max_end):
      for j in range(max_end):
        if i <= k <= j and graph[i][j] < graph[i][k] + graph[k][j]:
          graph[i][j] = graph[i][k] + graph[k][j]
  max_compensation = 0
  for i in range(max_end):
    for j in range(max_end):
      if max_compensation < graph[i][j]:
        max_compensation = graph[i][j]
  return max_compensation

if __name__ == "__main__":
  tc = int(input())
  for _ in range(tc):
    n = int(input())
    max_end = 49
    graph = [[0] * max_end for _ in range(max_end)]
    for _ in range(n):
      s, e, c = map(int, input().split())
      graph[s][e] = max(graph[s][e], c)
    result = floyd_warshall(graph, max_end)
    print(result)