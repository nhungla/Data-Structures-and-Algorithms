def find_start(matrix):
  for i, row in enumerate(matrix):
    for j, ch in enumerate(row):
      if ch == '@':
        return i, j
  return -1, -1
def solution(matrix, row, col):
  x_st, y_st = find_start(matrix)
  pool = [(x_st, y_st)]
  visited = set(pool)
  count = 0
  while pool:
    tmp = []
    for x, y in pool:
      count += 1
      for nx, ny in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
        if not(0 <= nx < row and 0 <= ny < col):
          continue
        if (nx, ny) in visited or matrix[nx][ny] == '#':
          continue
        tmp.append((nx, ny))
        visited.add(tmp[-1])
    pool = tmp
  return count
if __name__ == "__main__":
  tests = int(input())
  for i in range(tests):
    col, row = list(map(int, input().split()))
    matrix = []
    for j in range(row):
      matrix.append(list(input()))
    ans = solution(matrix, row, col)
    s = 'Case ' + str(i + 1) + ': ' + str(ans)
    print(s)