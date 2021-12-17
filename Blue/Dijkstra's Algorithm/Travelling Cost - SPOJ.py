import heapq
import collections

if __name__ == "__main__":
    n = int(input())
    gr = collections.defaultdict(list)
    for i in range(n):
        u, v, c = list(map(int, input().split()))
        gr[u].append((v, c))
        gr[v].append((u, c))

    start = int(input())
    u = int(input())
    ends = []
    for i in range(u):
        ends.append(int(input()))
    pool = [(start, 0)]
    dist = [float("inf")] * 501
    dist[start] = 0
    visited = set(pool)
    while pool:
        tmp = []
        for cur, cur_cost in pool:
            for ch, c in gr[cur]:
                if dist[ch] > c + cur_cost:
                    dist[ch] = c + cur_cost
                    heapq.heappush(tmp, (ch, c + cur_cost))
        pool = tmp
    for v in ends:
        print(dist[v]) if dist[v] != float("inf") else print("NO PATH")