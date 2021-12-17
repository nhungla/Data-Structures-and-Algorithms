def bellman(gr, n, m, juncs):
  costs = [float("inf")] * (n + 1)
  costs[1] = 0
  is_ne = False
  for i in range(n - 1):
    for u, v in gr:
      amount = (juncs[v] - juncs[u]) ** 3
      if costs[u] + amount < costs[v]:
        costs[v] = costs[u] + amount
  is_not_update = False
  while not is_not_update:
    is_not_update = True
    for u, v in gr:
      amount = (juncs[v] - juncs[u]) ** 3
      if costs[v] == float("-inf"):
        continue
      if costs[u] + amount < costs[v]:
        costs[v] = float("-inf")
        is_not_update = False
        break
  return costs
if __name__ == "__main__":
  tcs = int(input())
  for tc in range(tcs):
    _ = input()
    n = int(input())
    juncs = [0] + list(map(int, input().split()))
    m = int(input())
    gr = []
    for i in range(m):
      u, v = list(map(int, input().split()))
      gr.append((u, v))
    costs = bellman(gr, n, m, juncs)
    ss = "Case " + str(tc + 1) + ":"
    print(ss)
    q = int(input())
    for i in range(q):
      qu = int(input())
      if float("inf") > costs[qu] >= 3:
        print(costs[qu])
      else:
        print("?")
     # print(costs[qu]) if costs[qu] != float("inf") and costs[qu] >= 3 and neg[qu] is False else print("?")