def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i, w1 in enumerate(s1, 1):
        for j, w2 in enumerate(s2, 1):
            if w1 == w2:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp


def trace(s1, s2, i, j, dp, ans):
    if not i or not j:
        return
    if s1[i - 1] == s2[j - 1]:
        trace(s1, s2, i - 1, j - 1, dp, ans)
        ans.append(s1[i - 1])
    else:
        trace(s1, s2, i, j - 1, dp, ans) if dp[i][j - 1] > dp[i - 1][j] else trace(s1, s2, i - 1, j, dp, ans)


if __name__ == "__main__":
    while True:
        try:
            s1, s2 = input().split()
        except:
            break
        dp = lcs(s1, s2)
        n, m = len(s1), len(s2)
        ans = []
        trace(s1, s2, n, m, dp, ans)
        l1 = l2 = 0
        re = ''
        for i in range(len(ans)):
            while l1 < n and s1[l1] != ans[i]:
                re += s1[l1]
                l1 += 1
            while l2 < m and s2[l2] != ans[i]:
                re += s2[l2]
                l2 += 1
            re += ans[i]
            l1, l2 = l1 + 1, l2 +1
        while l1 < n:
            re += s1[l1]
            l1 += 1
        while l2 < m:
            re += s2[l2]
            l2 += 1
        print(re)
