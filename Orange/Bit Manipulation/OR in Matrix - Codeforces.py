if __name__ == "__main__":
    row, col = list(map(int, input().split()))
    matrix_B = []
    matrix_A, matrix_C = [[1] * col for _ in range(row)], [[0] * col for _ in range(row)]
    for _ in range(row):
        matrix_B.append(list(map(int, input().split())))
    for i in range(row):
        for j in range(col):
            if matrix_B[i][j] == 0:
                for k in range(col):
                    matrix_A[i][k] = 0
                for k in range(row):
                    matrix_A[k][j] = 0

    for i in range(row):
        for j in range(col):
            if matrix_A[i][j]:
                for k in range(col):
                    matrix_C[i][k] = 1
                for k in range(row):
                    matrix_C[k][j] = 1

    for i in range(row):
        for j in range(col):
            if matrix_C[i][j] != matrix_B[i][j]:
                print("NO")
                exit()

    print("YES")
    for r in matrix_A:
        print(" ".join(str(x) for x in r))
