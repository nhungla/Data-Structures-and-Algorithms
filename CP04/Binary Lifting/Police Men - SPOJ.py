import collections

LOG = 21


def dfs(graph, u, par, levels, parents):
    levels[u] = levels[par] + 1
    parents[u][0] = par
    for v in graph[u]:
        if v == par:
            continue
        dfs(graph, v, u, levels, parents)


def lca(u, v, parents, levels):
    if levels[u] < levels[v]:
        u, v = v, u
    for i in range(LOG, -1, -1):
        if (1 << i) <= levels[u] - levels[v]:
            u = parents[u][i]
    if u == v:
        return u
    for i in range(LOG - 1, -1, -1):
        if parents[u][i] != -1 and parents[u][i] != parents[v][i]:
            u, v = parents[u][i], parents[v][i]
    return parents[u][0]


if __name__ == "__main__":
    n = int(input())
    gr = collections.defaultdict(list)
    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        gr[u].append(v)
        gr[v].append(u)
    parents = [[-1] * LOG for _ in range(n + 1)]
    levels = [-1] * (n + 1)
    dfs(gr, 1, 0, levels, parents)
    for j in range(1, LOG):
        for i in range(1, n + 1):
            if parents[i][j - 1] != -1:
                parents[i][j] = parents[parents[i][j - 1]][j - 1]

    q = int(input())
    for _ in range(q):
        thief, police = list(map(int, input().split()))
        if thief == 1 and police == 1:
            print("YES 1")
        elif thief == 1 and police != 1 or levels[thief] < levels[police]:
            print("NO")
        else:
            print("YES %s" % lca(thief, police, parents, levels))
