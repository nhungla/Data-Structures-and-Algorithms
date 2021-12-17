import heapq
if __name__ == "__main__":
  n = int(input())
  for i in range(n):
    num_cont = int(input())
    arr = []
    pq = []
    for i in range(num_cont):
      arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x : x[2])
    ti, ans = 0, 0
    for a, b, d in arr:
      ti += b
      heapq.heappush(pq, (-a, b, d))
      while ti > d:
        ta, tb, td = heapq.heappop(pq)
        if tb > ti - d:
          tb -= ti - d
          ans +=  (ti - d) / -ta * 1.0
          ti = d
          heapq.heappush(pq, (ta, tb, td))
        else:
          ti -= tb
          ans += tb / -ta * 1.0
    print(format(ans, '.2f'))