def warshall(matrix, n):
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if i == j:
                    continue
                matrix[i][j] = max(matrix[i][j], matrix[i][k] * matrix[k][j])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if matrix[i][j] * matrix[j][i] > 1:
                return True
    return False


if __name__ == "__main__":
    tc = 0
    while True:
        tc += 1
        n = int(input())
        if n == 0:
            break
        map_idx = {}
        for i in range(n):
            map_idx[input()] = i
        m = int(input())
        matrix = [[0] * n for i in range(n)]
        for i in range(n):
            matrix[i][i] = 1
        for i in range(m):
            arr = list(input().split())
            u, v = map_idx[arr[0]], map_idx[arr[2]]
            matrix[u][v] = float(arr[1])
        is_available = warshall(matrix, n)
        ss = 'Case ' + str(tc) + ': '
        ss += 'Yes' if is_available else 'No'
        print(ss)
        input()
