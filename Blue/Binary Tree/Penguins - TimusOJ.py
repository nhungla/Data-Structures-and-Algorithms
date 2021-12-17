import collections
if __name__ == "__main__":
  n = int(input())
  counter = collections.Counter()
  for _ in range(n):
    counter[input()] += 1
  ans = ""
  max_val = float("-inf")
  for k, v in counter.items():
    if v > max_val:
      max_val = v
      ans = k
  print(ans)