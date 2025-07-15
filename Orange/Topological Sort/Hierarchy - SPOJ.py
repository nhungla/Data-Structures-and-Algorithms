import collections


def topological_sort(gr, n, ans):
    indeg = [0] * (n + 1)
    q = []
    for u in gr:
        for v in gr[u]:
            indeg[v] += 1
    for i, val in enumerate(indeg[1:], 1):
        if val == 0:
            q.append(i)
    while q:
        u = q.pop()
        ans.append(u)
        for v in gr[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    for i, val in enumerate(indeg[1:], 1):
        if val != 0:
            return False
    return True


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    gr = collections.defaultdict(list)
    for i in range(1, k + 1):
        tmp = list(map(int, input().split()))
        gr[i].extend(tmp[1:])
    ans = []
    re = topological_sort(gr, n, ans)
    p = 0
    par = [0] * (n + 1)
    for i in range(n):
        par[ans[i]] = p
        p = ans[i]
    for i in range(1, n + 1):
        print(par[i])
