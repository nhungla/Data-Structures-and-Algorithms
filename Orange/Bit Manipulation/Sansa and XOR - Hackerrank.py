if __name__ == "__main__":
  tc = int(input())
  for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for idx, val in enumerate(arr):
      time = (idx + 1) * (n - idx)
      if time & 1:
        ans ^= val
    print(ans)