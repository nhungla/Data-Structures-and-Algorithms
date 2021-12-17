if __name__ == "__main__":
  tc = int(input())
  for i in range(tc):
    matrix = [[ch for ch in input()]]
    m = len(matrix[0])
    for i in range(m - 1):
      matrix.append([ch for ch in input()])
    counter = [0] * m
    connected = [[False] * m for i in range(m)]
    for k in range(m):
      for i in range(m):
        if i == k:
          continue
        for j in range(m):
          if i == j or j == k:
            continue
          if matrix[i][j] == 'Y':
            continue
          if not connected[i][j] and matrix[i][k] == 'Y' and matrix[j][k] == 'Y':
            counter[i] += 1
            connected[i][j] = True
    max_fr = max(counter)
    ans = -1
    for i, v in enumerate(counter):
      if v == max_fr:
        ans = i
        break
    print(ans, max_fr)