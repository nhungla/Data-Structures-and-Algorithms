def count(mid, arr):
  ans = 0
  for val in arr:
    ans += max(val - mid, 0)
  return ans
if __name__ == "__main__":
  n, m = list(map(int, input().split()))
  arr = list(map(int, input().split()))
  l, r = 0, max(arr) + 1
  while l + 1 < r:
    mid = (l + r) >> 1
    if count(mid, arr) >= m:
      l = mid
    else:
      r = mid
  print(l)