if __name__ == "__main__":
  tc = int(input())
  for i in range(tc):
    n, m = list(map(int, input().split()))
    gr = []
    for j in range(m):
      u, v, ti = list(map(int, input().split()))
      gr.append((u, v, ti))
    dist = [float("inf")] * n
    dist[0] = 0
    holes = False
    for i in range(1, n):
      for j in range(m):
        s, e, c = gr[j][0], gr[j][1], gr[j][2]
        if dist[s] != float("inf") and dist[s] + c < dist[e]:
          dist[e] = dist[s] + c
    for j in range(m):
      s, e, c = gr[j][0], gr[j][1], gr[j][2]
      if dist[s] != float("inf") and dist[s] + c < dist[e]:
        holes = True
        break
    print("possible") if holes else print("not possible")