import heapq
if __name__ == "__main__":
  n = int(input())
  arr = []
  arr_re = []
  for i in range(n):
    query = list(map(int, input().split()))
    if arr and len(query) == 1:
      while arr_re and arr[0] == arr_re[0]:
        heapq.heappop(arr_re)
        heapq.heappop(arr)
      print(arr[0])
    else:
      k, v = query
      if k == 1:
        heapq.heappush(arr, v)
      if k == 2:
        heapq.heappush(arr_re, v)
        