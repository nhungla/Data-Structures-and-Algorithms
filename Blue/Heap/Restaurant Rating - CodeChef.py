import heapq
if __name__ == "__main__":
  n = int(input())
  arr = []
  count = 0
  ans = []
  for i in range(n):
    query = list(map(int, input().split()))
    if len(query) == 1:
      if not ans:
        print("No reviews yet")
      else:
        print(ans[0])
    else:
      k, v = query
      count += 1
      if ans and ans[0] < v:
        heapq.heappush(arr, -heapq.heappop(ans))
        heapq.heappush(ans, v)
      else:
        heapq.heappush(arr, -v)
      if count % 3 == 0:
        heapq.heappush(ans, -heapq.heappop(arr))