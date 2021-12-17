import collections
import heapq


def prim(gr, st):
    dists = collections.defaultdict(lambda: float("inf"))
    dists[st] = 0
    visited = collections.defaultdict(lambda: False)
    pool = [(0, st)]
    while pool:
        c, cur = heapq.heappop(pool)
        visited[cur] = True
        for ch, cost in gr[cur]:
            if visited[ch]:
                continue
            if dists[ch] > cost:
                dists[ch] = cost
                heapq.heappush(pool, (cost, ch))
    ans = 0
    for u in gr:
        if dists[u] == float("inf"):
            return -1
        ans += dists[u]
    return ans


if __name__ == "__main__":
    tc = int(input())
    for t in range(1, tc + 1):
        input()
        m = int(input())
        gr = collections.defaultdict(list)
        st = None
        for _ in range(m):
            u, v, c = input().split()
            if st is None:
                st = u
            gr[u].append((v, int(c)))
            gr[v].append((u, int(c)))
        ans = prim(gr, st) if prim(gr, st) != -1 else "Impossible"
        print("Case %s: %s" % (t, ans))
