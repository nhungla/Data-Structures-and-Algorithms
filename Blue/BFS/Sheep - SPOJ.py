def bfs(graph, xs, ys, n, m, used):
  pool = [(xs, ys)]
  used.add((xs, ys))
  sheep, woft = int(graph[xs][ys] == 'k'), int(graph[xs][ys] == 'v')
  is_unharmed = False
  while pool:
    tmp = []
    for x, y in pool:
      for nx, ny in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
        if not(0 <= nx < n and 0 <= ny < m):
          is_unharmed = True
          continue
        if (nx, ny) in used:
          continue
        if graph[nx][ny] == '#':
          continue
        if graph[nx][ny] == 'k':
          sheep += 1
        if graph[nx][ny] == 'v':
          woft += 1
        used.add((nx, ny))
        tmp.append((nx, ny))
    pool = tmp
  return woft, sheep, is_unharmed
if __name__ == "__main__":
  n, m = list(map(int, input().split()))
  graph = []
  for i in range(n):
    graph.append(list(input()))
  used = set()
  woft, sheep = 0, 0
  for i, row in enumerate(graph):
    for j, val in enumerate(row):
      if (i, j) in used or val == '#':
        continue
      w, s, is_unharmed = bfs(graph, i, j, n, m, used)
      if is_unharmed:
        woft, sheep = woft + w, sheep + s
      else:
        if w >= s:
          woft += w
        else:
          sheep += s
  print(sheep, woft)