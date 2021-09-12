LOG = 21


def find_kth_parent(pars, n):
    parents = [[-1] * LOG for _ in range(n)]
    for i, val in enumerate(pars):
        parents[i][0] = val
    for j in range(1, LOG):
        for i in range(n):
            if parents[i][j - 1] != -1:
                parents[i][j] = parents[parents[i][j - 1]][j - 1]
    return parents


def query(node, k, parents):
    for i in range(LOG - 1, -1, -1):
        if node == -1:
            return -1
        if (1 << i) & k:
            node = parents[node][i]
    return node


if __name__ == "__main__":
    n = int(input())
    pars = list(map(int, input().split()))
    parents = find_kth_parent(pars, n)
    while True:
        try:
            node, k = list(map(int, input().split()))
        except:
            break
        print(query(node, k, parents))
