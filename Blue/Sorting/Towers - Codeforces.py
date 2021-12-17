if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  counters = {}
  max_val = 0
  for val in arr:
    counters[val] = counters.get(val, 0) + 1
    max_val = max(max_val, counters[val])
  print(max_val, len(counters))