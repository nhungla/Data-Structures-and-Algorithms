import heapq
if __name__ == "__main__":
  while True:
    n = int(input())
    if n == 0:
      break
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    ans = 0
    while len(arr) > 1:
      a = heapq.heappop(arr)
      b = heapq.heappop(arr)
      ans += a + b
      heapq.heappush(arr, a + b)
    print(ans)