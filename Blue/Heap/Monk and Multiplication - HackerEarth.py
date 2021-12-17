import heapq
if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  ans = []
  pq = []
  for i, val in enumerate(arr):
    heapq.heappush(pq, -val)
    if i < 2:
      ans.append(-1)
    else:
      first, second, third = heapq.heappop(pq), heapq.heappop(pq), heapq.heappop(pq)
      ans.append(first * second * third * (-1))
      heapq.heappush(pq, first)
      heapq.heappush(pq, second)
      heapq.heappush(pq, third)
  for i in range(n):
    print(ans[i])