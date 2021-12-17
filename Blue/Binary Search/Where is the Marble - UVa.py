def search(arr, target):
  l, r = -1, len(arr) - 1
  while l + 1 < r:
    mid = (l + r) >> 1
    if target <= arr[mid]:
      r = mid
    else:
      l = mid
  return r if arr[r] == target else -1
if __name__ == "__main__":
  tc = 0
  while True:
    tc += 1
    n, q = list(map(int, input().split()))
    if n == q == 0:
      break
    arr = []
    for i in range(n):
      arr.append(int(input()))
    arr.sort()
    print("CASE# %s:" % tc)
    for i in range(q):
      qu = int(input())
      ans = search(arr, qu)
      if ans == -1:
        print("%s not found" % qu)
      else:
        print("%s found at %s" % (qu, ans + 1))