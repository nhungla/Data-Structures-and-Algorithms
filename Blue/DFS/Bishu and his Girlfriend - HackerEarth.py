MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for _ in range(MAX)]


def DFS(scr):
    s = [scr]
    visited[scr] = True

    while len(s):
        u = s.pop()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                s.append(v)


V = int(input())
E = V - 1

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(1)
ans = 0
min_dist = MAX

Q = int(input())

for _ in range(Q):
    u = int(input())
    if dist[u] < min_dist or (dist[u] == min_dist and u < ans):
        min_dist = dist[u]
        ans = u

print(ans)