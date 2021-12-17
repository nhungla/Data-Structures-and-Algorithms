if __name__ == "__main__":
  tc = int(input())
  for _ in range(tc):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    s = set(arr[:n])
    for val in arr[n:]:
      if val in s:
        print("YES")
      else:
        print("NO")
      s.add(val)