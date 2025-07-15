def is_valid(x, y, a, b, idx):
    for i in range(idx):
        if abs(x[i] - a) == abs(y[i] - b):
            return False
    return True


def dfs(matrix, idx, ss, ans, x, y):
    if idx == 8:
        ans[0] = max(ss, ans[0])
        return
    for i in range(8):
        if used[i] or not is_valid(x, y, idx, i, idx):
            continue
        used[i] = True
        x[idx], y[idx] = idx, i
        dfs(matrix, idx + 1, ss + matrix[idx][i], ans, x, y)
        used[i] = False


if __name__ == "__main__":
    num_of_tab = int(input())
    for _ in range(num_of_tab):
        matrix = []
        for _ in range(8):
            matrix.append(list(map(int, input().split())))
        x, y = [0] * 8, [0] * 8
        used = [False] * 8
        ans = [0]
        dfs(matrix, 0, 0, ans, x, y)
        print("   %s" % ans[0])
