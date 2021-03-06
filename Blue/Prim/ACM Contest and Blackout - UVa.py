import queue


class node:
    dist = 0
    index = 0

    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist


def inp():
    return map(int, input().split())


def prim(graph, src):
    n = len(graph)
    dist = [1e18 for i in range(n)]
    visited = [0 for i in range(n)]
    total_cost = 0
    dist[src] = 0
    Q = queue.PriorityQueue()
    Q.put(node(0, src))
    trace = [{} for i in range(n)]
    while not Q.empty():
        temp = Q.get()
        u = temp.index
        visited[u] = True
        _len = len(graph[u])
        for i in range(_len):
            v = graph[u][i].index
            if not visited[v] and dist[v] > graph[u][i].dist:
                dist[v] = graph[u][i].dist
                Q.put(node(dist[v], v))
                trace[v] = {'path': u, 'index': i}
    for i in range(n):
        total_cost += dist[i]
    return total_cost, trace

def inp():
    return map(int, input().split())

def solve():
    testcase = int(input())
    inf = 1e9
    for t in range(testcase):
        n, m = inp()
        graph = [[] for i in range(n)]
        for i in range(m):
            u, v, cost = inp()
            u-=1
            v-=1
            graph[u].append(node(cost, v))
            graph[v].append(node(cost, u))
        trace = []
        min1, trace = prim(graph, 0)
#         xoa canh bang cach thay cac canh do bang inf
        min2 = inf
        for j in range(1, n):
            item = trace[j]
            u = item['path']
            i = item['index']
            temp = graph[u][i].dist
            graph[u][i].dist = inf
            val, temp_trace = prim(graph, 0)
            graph[u][i].dist = temp
            min2 = min(min2, val)

        print('{} {}'.format(min1, min2))
solve()