import math
def warshall(matrix, n):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if matrix[i][j] > matrix[i][k] + matrix[k][j]:
          matrix[i][j] = matrix[i][k] + matrix[k][j]
if __name__ == "__main__":
  tc = int(input())
  for t in range(tc):
    n = int(input())
    arr = []
    for i in range(n):
      x, y = list(map(int, input().split()))
      arr.append((x, y))
    matrix = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        x1, y1 = arr[i]
        x2, y2 = arr[j]
        tmp = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if tmp <= 10:
          #matrix[i][j] = matrix[j][i] = tmp
          matrix[i][j] = tmp
    warshall(matrix, n)
    ans = 0
    for i in range(n):
      for j in range(n):
        if matrix[i][j] > ans:
          ans = matrix[i][j]
    ss = "Case #" + str(t + 1) + ":"
    print(ss)
    if ans == float("inf"):
      print("Send Kurdy")
    else:
      print(format(ans, ".4f"))
    print("")