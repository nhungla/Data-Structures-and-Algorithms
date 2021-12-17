def lcs(s1, s2, k):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i, w1 in enumerate(s1, 1):
        for j, w2 in enumerate(s2, 1):
            if w1 == w2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
            f[i][j] = max(f[i][j - 1], f[i - 1][j])
            for e in range(k, dp[i][j] + 1):
                f[i][j] = max(f[i][j], f[i - e][j - e] + e)
    return dp, f


if __name__ == "__main__":
    while True:
        k = int(input())
        if k == 0:
            break
        s1, s2 = input(), input()
        _, f = lcs(s1, s2, k)
        print(f[-1][-1])
