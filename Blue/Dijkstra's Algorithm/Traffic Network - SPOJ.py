import heapq, collections


def dijikstra(gr, start):
    dist = [float("inf")] * (n + 1)
    used = [False] * (n + 1)
    pool = [(start, 0)]
    dist[start] = 0
    while pool:
        cur, cur_cost = heapq.heappop(pool)
        used[cur] = True
        for ch, ch_cost in gr[cur]:
            if not used[ch] and dist[ch] > dist[cur] + ch_cost:
                dist[ch] = dist[cur] + ch_cost
                heapq.heappush(pool, (ch, dist[ch]))
    return dist


if __name__ == "__main__":
    testcases = int(input())
    for i in range(testcases):
        n, m, k, s, t = list(map(int, input().split()))
        gr_s, gr_t = collections.defaultdict(list), collections.defaultdict(list)
        for j in range(m):
            u, v, c = list(map(int, input().split()))
            gr_s[u].append((v, c))
            gr_t[v].append((u, c))
        dist_s = dijikstra(gr_s, s)
        dist_t = dijikstra(gr_t, t)
        ans = dist_s[t]
        for j in range(k):
            u, v, c = list(map(int, input().split()))
            ans = min(ans, dist_s[u] + dist_t[v] + c, dist_s[v] + dist_t[u] + c)
        print(ans) if ans != float("inf") else print(-1)
