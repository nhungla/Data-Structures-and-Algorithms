def bellman(gr, n, s):
  costs = [float("-inf")] * (n + 1)
  costs[s] = 0
  for i in range(n):
    for u, v, c in gr:
      if costs[v] < costs[u] + c:
        costs[v] = costs[u] + c
        if i == n -1:
          return True
  return False
if __name__ == "__main__":
  tc = int(input())
  for i in range(tc):
    n, m = list(map(int, input().split()))
    gr = []
    for i in range(m):
      u, v, c = list(map(int, input().split()))
      gr.append((u, v, c))
    ans = bellman(gr, n, 1)
    print("Yes" if ans else "No")