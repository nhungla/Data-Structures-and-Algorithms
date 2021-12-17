if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        n, w = list(map(int, input().split()))
        ques = [[0, 0, 0]]
        for _ in range(n):
            ques.append(list(map(int, input().split())))
        dp = [[0] * (w + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            count, point, time = ques[i]
            for j in range(1, w + 1):
                if time <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + count * point)
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp[-1][-1])
