import collections
import heapq


def dijkstra(gr, n, s, e):
    dists = [float("inf")] * n
    dists[s] = 0
    pool = [(0, s)]
    while pool:
        cur_d, cur = heapq.heappop(pool)
        if cur_d > dists[cur]:
            continue
        for ch, d in gr[cur]:
            if cur_d + d < dists[ch]:
                dists[ch] = cur_d + d
                heapq.heappush(pool, (dists[ch], ch))
    return dists[e]


if __name__ == "__main__":
    tcs = int(input())
    for tc in range(1, tcs + 1):
        n, m, s, t = list(map(int, input().split()))
        gr = collections.defaultdict(list)
        for _ in range(m):
            a, b, w = list(map(int, input().split()))
            gr[a].append((b, w))
            gr[b].append((a, w))
        tmp = dijkstra(gr, n, s, t)
        ans = tmp if tmp < float("inf") else "unreachable"
        print("Case #%s: %s" % (tc, ans))
