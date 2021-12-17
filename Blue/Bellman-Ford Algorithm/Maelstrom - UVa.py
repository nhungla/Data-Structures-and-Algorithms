if __name__ == "__main__":
  n = int(input())
  gr = [[float("inf")] * n for _ in range(n)]
  for i in range(n):
    gr[i][i] = 0
  for j in range(1, n):
    i = 0
    arr = list(input().split())
    for v in arr:
      if v != 'x':
        gr[i][j] = gr[j][i] = int(v)
      else:
        gr[i][j] = gr[j][i] = float("inf")
        #gr[i][j] = gr[j][i] = 'x'
      i += 1
  #print(gr)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        #if gr[i][j] != float("-inf") and gr[i][k] != float("-inf") and gr[k][j] != float("-inf"):
          #gr[i][j] = min(gr[i][j], gr[i][k] + gr[k][j])
        gr[i][j] = min(gr[i][j], gr[i][k] + gr[k][j])
  ans = 0
  #print(gr)
  for i in range(1, n):
    if gr[0][i] != float("inf"):
      ans = max(ans, gr[0][i])
  print(ans)