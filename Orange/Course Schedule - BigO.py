import collections

NOT_VISITED = 0
PROCESSING = 1
VISITED = 2


def is_has_circle(graph, cur, colors):
    colors[cur] = PROCESSING
    for ne in graph[cur]:
        if colors[ne] == NOT_VISITED:
            check = is_has_circle(graph, ne, colors)
            if not check:
                return False
        elif colors[ne] == PROCESSING:
            return False
    colors[cur] = VISITED
    return True


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    prerequisites = collections.defaultdict(list)
    for _ in range(m):
        u, v = list(map(int, input().split()))
        prerequisites[u].append(v)
    colors = [NOT_VISITED] * n
    ans = True
    for i in range(n):
        if colors[i] == NOT_VISITED and not is_has_circle(prerequisites, i, colors):
            ans = False
            break
    print("yes" if ans else "no")
