if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  b = sorted(arr)
  l, r = 0, n - 1
  while l < r:
    if b[l] != arr[l]:
      break
    l += 1
  while l < r:
    if b[r] != arr[r]:
      break
    r -= 1
  start, end = l + 1, r + 1
  while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l, r = l + 1, r - 1
  if b == arr:
    print('yes')
    if start == end:
      start = end = 1
    print(start, end)
  else:
    print('no')  