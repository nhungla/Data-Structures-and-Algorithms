import collections
import heapq

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    gr = collections.defaultdict(list)
    for _ in range(m):
        u, v, c = list(map(int, input().split()))
        gr[u - 1].append((v - 1, c))
        gr[v - 1].append((u - 1, c))
    s = int(input()) - 1
    pool = [(0, s)]
    visited = [False] * n
    dists = [float("inf")] * n
    dists[s] = 0
    while pool:
        c, cur = heapq.heappop(pool)
        visited[cur] = True
        for ch, cost in gr[cur]:
            if visited[ch]:
                continue
            if dists[ch] > cost:
                dists[ch] = cost
                heapq.heappush(pool, (cost, ch))
    ans = sum(dists)
    print(ans if ans < float("inf") else 0)
