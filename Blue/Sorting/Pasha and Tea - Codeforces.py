if __name__ == "__main__":
  inputs = list(map(int, input().split()))
  n, w = inputs[0], inputs[1]
  arr = list(map(int, input().split()))
  arr.sort()
  m = arr[n]
  if arr[0] * 2 < m:
  	ans = arr[0] * n + 2 * arr[0] * n
  else:
    ans = (m / 2.0) * n + m * n
  print(ans) if ans <= w else print(w)