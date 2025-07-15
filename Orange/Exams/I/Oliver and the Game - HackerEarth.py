import sys
sys.setrecursionlimit(100000000)
t = 0
def dfs(graph, start_time, finish_time, v):
    global t
    t += 1
    start_time[v] = t
    for u in graph[v]:
        if start_time[u] == 0:
            dfs(graph, start_time, finish_time, u)
    finish_time[v] = t

if __name__ == '__main__':
    n = int(input())
    graph = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    start_time = [0] * n
    finish_time = [0] * n
    dfs(graph, start_time, finish_time, 0)
    q = int(input())
    for i in range(q):
        s, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if s == 1:
            a, b = b, a
        if start_time[a] <= start_time[b] and finish_time[a] >= start_time[b]:
            print('YES')
        else:
            print('NO')