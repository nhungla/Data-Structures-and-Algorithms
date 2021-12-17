def is_ok(mid, arr, k):
  inc, desc = 0.0, 0.0
  for val in arr:
    if val > mid:
      inc += val - mid
    else:
      desc += mid - val
  return inc - (inc * k) / 100.0 >= desc
if __name__ == "__main__":
  n, k = list(map(int, input().split()))
  arr = list(map(int, input().split()))
  error = 10 ** (-10)
  l, r = min(arr) * 1.0, max(arr) * 1.0 + error
  while l + error < r:
    mid = (l + r) / 2
    if is_ok(mid, arr, k):
      l = mid
    else:
      r = mid
  print(format(l, ".9f"))