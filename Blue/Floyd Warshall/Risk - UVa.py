def warshall(matrix):
    for k in range(1, 21):
        for i in range(1, 21):
            for j in range(1, 21):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


def get_format(x):
    if x >= 10:
        return "%s" % x
    return " %s" % x


def solve():
    count = 0
    while True:
        count += 1
        matrix = [[float("inf")] * 21 for i in range(21)]
        for i in range(1, 20):
            arr = list(map(int, input().split()))
            for val in arr[1:]:
                matrix[i][val] = matrix[val][i] = 1
        warshall(matrix)
        print("Test Set #%s" % count)
        n = int(input())
        for i in range(n):
            x, y = list(map(int, input().split()))
            a = get_format(x)
            b = get_format(y)
            print("%s to %s: %s" % (a, b, matrix[x][y]))
        print()


if __name__ == "__main__":
    try:
        solve()
    except Exception as ex:
        #  print(ex)
        pass