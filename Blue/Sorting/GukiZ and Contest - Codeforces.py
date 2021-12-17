if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  sorted_arr = sorted(arr)
  map_idx = {}
  for idx, val in enumerate(sorted_arr):
    map_idx[val] = idx
  ans = []
  for idx, val in enumerate(arr):
    ans.append((n - map_idx[val]))
  for e in ans:
    print(e, end=" ")