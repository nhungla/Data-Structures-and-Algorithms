if __name__ == "__main__":
  tc = int(input())
  for i in range(tc):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    l, r = 0, n - 1
    ans = 0
    while l < r:
      if arr[l] + arr[r] == m:
        ans += 1
        l, r = l + 1, r - 1
      elif arr[l] + arr[r] > m:
        r -= 1
      else:
        l += 1
    print(ans)