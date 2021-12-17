def find(arr, h):
  lo, hi = 0, 0
  l, r = 0, len(arr)
  while l + 1 < r:
    mid = (l + r) >> 1
    if arr[mid] < h:
      l = mid
    else:
      r = mid
  hi = arr[l] if arr[l] < h else 'X'
  l, r = -1, len(arr) - 1
  while l + 1 < r:
    mid = (l + r) >> 1
    if arr[mid] > h:
      r = mid
    else:
      l = mid
  lo = arr[r] if arr[r] > h else 'X'
  return hi, lo
if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  q = int(input())
  query = list(map(int, input().split()))
  for val in query:
    hi, lo = find(arr, val)
    print(hi, lo)