if __name__ == "__main__":
  k = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  total = 0
  count = 0
  for i in range(len(arr) - 1, -1, -1):
    if total >= k:
      break
    total += arr[i]
    count += 1
  print(count) if total >= k else print(-1)