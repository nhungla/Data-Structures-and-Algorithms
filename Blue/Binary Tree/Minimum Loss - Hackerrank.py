if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  map_idx = {}
  for idx, val in enumerate(arr):
    map_idx[val] = idx
  ss = sorted(arr)
  min_cost = float("inf")
  for i in range(1, n):
    if map_idx[ss[i]] < map_idx[ss[i - 1]]:
      min_cost = min(min_cost, ss[i] - ss[i - 1])
  print(min_cost)