def warshall(matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


if __name__ == "__main__":
    tc = 0
    while True:
        n = int(input())
        tc += 1
        if n == 0:
            break
        name_idx = {}
        distances = []
        for i in range(n):
            arr = list(map(str, input().split()))
            name_idx[i] = arr[0]
            distances.append(list(map(int, arr[1:])))
        # gr = collections.defaultdict(list)
        # gr = []
        matrix = [[float("inf")] * n for _ in range(n)]
        co_matrix = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            for u, c in enumerate(distances[i]):
                # gr.append((i, u, c))
                if i != u and c == 0:
                    continue
                matrix[i][u] = c
            if matrix[i][i] > 0:
                matrix[i][i] = 0
        warshall(matrix, n)
        for i in range(n):
            for j in range(n):
                co_matrix[i][j] = matrix[i][j]
        warshall(matrix, n)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != co_matrix[i][j]:
                    matrix[i][j] = float("-inf")
        warshall(matrix, n)
        q = int(input())
        ss = "Case #" + str(tc) + ":"
        print(ss)
        for i in range(q):
            start, end = list(map(int, input().split()))
            if matrix[start][end] == float("-inf") and matrix[start][end] != co_matrix[start][end]:
                print("NEGATIVE CYCLE")
            elif matrix[start][end] == float("inf"):
                sss = name_idx[start] + "-" + name_idx[end] + " NOT REACHABLE"
                print(sss)
            else:
                sss = name_idx[start] + "-" + name_idx[end] + " " + str(matrix[start][end])
                print(sss)
