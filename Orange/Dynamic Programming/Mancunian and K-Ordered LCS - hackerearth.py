def main():
    n, m, k = map(int, input().split())
    assert 1 <= n <= 2000, n
    assert 1 <= m <= 2000, m
    assert 1 <= k <= 5, k
    a = list(map(int, input().split()))
    assert all(1 <= x <= 1e9 for x in a)
    b = list(map(int, input().split()))
    assert all(1 <= x <= 1e9 for x in b)

    dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            for t in range(k + 1):
                if i == 0 or j == 0:
                    dp[i][j][t] = 0
                elif a[i - 1] == b[j - 1]:
                    dp[i][j][t] = dp[i - 1][j - 1][t] + 1
                else:
                    dp[i][j][t] = max(dp[i - 1][j][t], dp[i][j - 1][t])
                    if t > 0:
                        dp[i][j][t] = max(dp[i][j][t], dp[i - 1][j - 1][t - 1] + 1)
    print(dp[n][m][k])


if __name__ == "__main__":
    main()