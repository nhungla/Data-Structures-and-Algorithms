import heapq
import math
import collections


def find_dist(a, b):
    xa, ya = a
    xb, yb = b
    return math.sqrt((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb))


def prim(points, n):
    visited = [False] * n
    dists = [float("inf")] * n
    dists[0] = 0
    pool = [(0, 0)]
    while pool:
        cur_dist, cur = heapq.heappop(pool)
        visited[cur] = True
        for ch, dist in gr[cur]:
            if visited[ch]:
                continue
            if dists[ch] > dist:
                dists[ch] = dist
                heapq.heappush(pool, (dist, ch))
    return sum(dists)


if __name__ == "__main__":
    try:
        while True:
            n = int(input())
            points = []
            gr = collections.defaultdict(list)
            check = set()
            for _ in range(n):
                x, y = list(map(int, input().split()))
                points.append((x, y))
            m = int(input())
            for _ in range(m):
                u, v = list(map(int, input().split()))
                gr[u - 1].append((v - 1, 0))
                gr[v - 1].append((u - 1, 0))
                check.add((u - 1, v - 1))
            for i in range(n):
                for j in range(i + 1, n):
                    if (i, j) in check:
                        continue
                    d = find_dist(points[i], points[j])
                    gr[i].append((j, d))
                    gr[j].append((i, d))
            ans = prim(points, n)
            print(format(ans, ".2f"))
    except:
        pass