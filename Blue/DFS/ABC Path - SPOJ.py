import sys
sys.setrecursionlimit(10000000)

DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

case = 0
while True:
    case += 1
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    a = []
    for i in range(h):
        a.append(input())
    dist = [[0] * w for i in range(h)]

    def find_path(u, v):
        if dist[u][v]:
            return dist[u][v]
        max_path = 0
        for dx, dy in DIR:
            n_u, n_v = u + dx, v + dy
            if n_u < 0 or n_u >= h or n_v < 0 or n_v >= w or ord(a[n_u][n_v]) != ord(a[u][v]) + 1:
                continue
            max_path = max(max_path, find_path(n_u, n_v))
        dist[u][v] = max_path + 1
        return dist[u][v]

    res = 0
    for x in range(h):
        for y in range(w):
            if a[x][y] == 'A':
                res = max(res, find_path(x, y))
    print('Case {}: {}'.format(case, res))