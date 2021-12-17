def warshall(matrix, n):
  for k in range(n):
    for i in range(n):
      if k == i:
        continue
      for j in range(n):
        if j == i:
          continue
        tmp_cost = matrix[i][k] + matrix[k][j]
        tmp_lar = max(large_ma[i][k], large_ma[k][j])
        if tmp_cost + tmp_lar < matrix[i][j] + large_ma[i][j]: 
          matrix[i][j] = matrix[j][i] = tmp_cost
          large_ma[i][j] = large_ma[j][i] = tmp_lar
if __name__ == "__main__":
  tc = 0
  while True:
    tc += 1
    c, r, q = list(map(int, input().split()))
    if c == r == q == 0:
      break
    costs = list(map(int, input().split()))
    matrix = [[float("inf")] * c for i in range(c)]
    large_ma = [[float("inf")] * c for i in range(c)]
    for i in range(c):
      large_ma[i][i] = costs[i]
    for i in range(r):
      u, v, co = list(map(int, input().split()))
      matrix[u - 1][v - 1] = matrix[v - 1][u - 1] = co
      large_ma[u - 1][v - 1] = large_ma[v - 1][u - 1] = max(costs[u - 1], costs[v - 1])
    warshall(matrix, c)
    warshall(matrix, c)
    ss = "Case #" + str(tc)
    print("\n" + ss) if tc != 1 else print(ss)
    for i in range(q):
      s, e = list(map(int, input().split()))
      ans = matrix[s - 1][e - 1] + large_ma[s - 1][e - 1] if matrix[s - 1][e - 1] < float("inf") else -1
      print(ans)