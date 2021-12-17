import math
if __name__ == "__main__":
  n, s = list(map(int, input().split()))
  target = 1000000 - s
  arr = []
  for _ in range(n):
    x, y, k = list(map(int, input().split()))
    arr.append((x * x + y * y, k))
  arr.sort()
  idx = 0
  ans = 0.0
  while target > 0:
    if idx >= n:
      break
    r, k = arr[idx]
    ans = math.sqrt(r)
    target -= k
    idx += 1
  print(format(ans, ".7f") if target <= 0 else -1)