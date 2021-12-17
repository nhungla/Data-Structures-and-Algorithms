import queue

MAX = 105
INF = int(1e9) + 7
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]


class Node:
    def __init__(self, _id, _weight):
        self.id = _id
        self.weight = _weight

    def __lt__(self, other):
        return self.weight < other.weight


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.weight

        for neighbor in graph[u]:
            if w + neighbor.weight < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.weight
                pq.put(Node(neighbor.id, dist[neighbor.id]))


N = int(input())
E = int(input())
T = int(input())
M = int(input())
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append(Node(u, w))

Dijkstra(E)

count = 0
for i in range(1, N + 1):
    if dist[i] <= T:
        count += 1

print(count)