if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        n, m = list(map(int, input().split()))
        stones = []
        for _ in range(n):
            stones.append(list(map(int, input().split())))
        for i in range(1, n):
            for j in range(m):
                cur = stones[i][j]
                if j:
                    stones[i][j] = max(stones[i][j], cur + stones[i - 1][j - 1])
                if j < m - 1:
                    stones[i][j] = max(stones[i][j], cur + stones[i - 1][j + 1])
                stones[i][j] = max(stones[i][j], cur + stones[i - 1][j])
        print(max(stones[-1]))
