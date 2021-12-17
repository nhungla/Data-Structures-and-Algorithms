def warshall(matrix, n, arr):
  visited = [False] * n
  ans = [0] * len(arr)
  for i in range(n - 1, -1, -1):
    add = arr[i] - 1
    visited[add] = True
    for j in range(n):
      for k in range(n):
        matrix[j][k] = min(matrix[j][k], matrix[j][add] + matrix[add][k])
    for j in range(n):
      for k in range(n):
        if visited[j] and visited[k]:
          ans[i] += matrix[j][k]
  return ans
if __name__ == "__main__":
  n = int(input())
  matrix = []
  for i in range(n):
    matrix.append(list(map(int, input().split())))
  remove = list(map(int, input().split()))
  ans = warshall(matrix, n, remove)
  ss = ' '.join(list(map(str, ans)))
  print(ss)