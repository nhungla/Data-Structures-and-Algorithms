def is_valid(mid, arr):
  for idx in range(1, len(arr)):
    if arr[idx] - arr[idx - 1] == mid:
      mid -=1
    elif arr[idx] - arr[idx - 1] > mid:
      return False
  return True
if __name__ == "__main__":
  tc = int(input())
  for i in range(tc):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    l, r = 0, 10 ** 7
    while l + 1 < r:
      mid = (l + r) >> 1
      if is_valid(mid, arr):
        r = mid
      else:
        l = mid
    print("Case %s: %s" % (i + 1, r))