import collections
import heapq


def prim(gr):
    pool = [(0, 0)]
    visited = [False] * n
    visited[0] = True
    dists = [float("inf")] * n
    dists[0] = 0
    while pool:
        c, u = heapq.heappop(pool)
        visited[u] = True
        for ch, cost in gr[u]:
            if visited[ch]:
                continue
            if dists[ch] > cost:
                dists[ch] = cost
                heapq.heappush(pool, (cost, ch))
    return sum(dists)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    gr = collections.defaultdict(list)

    for _ in range(m):
        u, v, c = list(map(int, input().split()))
        gr[u - 1].append((v - 1, c))
        gr[v - 1].append((u - 1, c))
    ans = prim(gr)
    print(ans)