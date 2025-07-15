import collections
import heapq


def topological_sort(gr, ans, n):
    indegree = [0] * (n + 1)
    q = []
    for u in gr:
        for v in gr[u]:
            indegree[v] += 1
    for i, val in enumerate(indegree[1:], 1):
        if val == 0:
            heapq.heappush(q, i)
    while q:
        u = heapq.heappop(q)
        ans.append(u)
        for v in gr[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(q, v)
    for i, val in enumerate(indegree[1:], 1):
        if val != 0:
            return False
    return True


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    gr = collections.defaultdict(list)
    for _ in range(m):
        u, v = list(map(int, input().split()))
        gr[u].append(v)
    ans = []
    re = topological_sort(gr, ans, n)
    print(" ".join(str(val) for val in ans) if re else "Sandro fails.")
