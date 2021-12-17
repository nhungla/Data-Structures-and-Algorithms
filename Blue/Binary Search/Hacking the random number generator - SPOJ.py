def search(arr, target, l, r):
  while l + 1 < r:
    mid = (l + r) >> 1
    if arr[mid] <= target:
      l = mid
    else:
      r = mid
  return True if arr[l] == target else False
if __name__ == "__main__":
  n, k = list(map(int, input().split()))
  arr = list(map(int, input().split()))
  ans = 0
  arr.sort()
  for idx, val in enumerate(arr[:n - 1]):
    if search(arr, val + k, idx + 1, n):
      ans += 1
    if search(arr, val - k, idx + 1, n):
      ans += 1
  print(ans)