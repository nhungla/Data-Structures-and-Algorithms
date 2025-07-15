import collections


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i, w1 in enumerate(s1, 1):
        for j, w2 in enumerate(s2, 1):
            if w1 == w2:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[n][m]


if __name__ == "__main__":
    s = input()
    print(len(s) - lcs(s, s[::-1]))
