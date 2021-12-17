def bellman(gr, start, n):
  dists = [float("inf")] * n
  dists[start] = 0
  for i in range(n):
    for u, v, w in gr:
      if dists[v] > dists[u] + w:
        dists[v] = dists[u] + w
  is_not_update = False
  while not is_not_update:
    is_not_update = True
    for u, v, w in gr:
      if dists[v] > dists[u] + w:
        dists[v] = float("-inf")
        is_not_update = False
        break
  return dists
if __name__ == "__main__":
  while True:
    n, m, q, s = list(map(int, input().split()))
    if n == m == q == s == 0:
      break
    gr = []
    for i in range(m):
      u, v, w = list(map(int, input().split()))
      gr.append((u, v, w))
    dists = bellman(gr, s, n)
    for i in range(q):
      query = int(input())
      if dists[query] == float("-inf"):
        print("-Infinity")
      elif dists[query] == float("inf"):
        print("Impossible")
      else:
        print(dists[query])
    print("")