import collections
def solution(matrix, row, col, n, m):
  pool = [(row, col)]
  ans = 0
  while pool:
    tmp = []
    for x, y in pool:
      ans += 1
      matrix[x][y] = 0
      for nx, ny in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
        if not(0 <= nx < n and 0 <= ny < m):
          continue
        if matrix[nx][ny] == 0:
          continue
        tmp.append((nx, ny))
        matrix[nx][ny] = 0
    pool = tmp
  return ans
if __name__ == "__main__":
  n, m = list(map(int, input().split()))
  while (n, m) != (0, 0):
    matrix = []
    ans = []
    for i in range(n):
      matrix.append(list(map(int, input().split())))
    for i, row in enumerate(matrix):
      for j, val in enumerate(row):
        if matrix[i][j]:
          count = solution(matrix, i, j, n, m)
          ans.append(count)
    ans.sort()
    print(len(ans))
    counter = collections.Counter(ans)
    for val in counter:
      print(val, counter[val])
    n, m = list(map(int, input().split()))