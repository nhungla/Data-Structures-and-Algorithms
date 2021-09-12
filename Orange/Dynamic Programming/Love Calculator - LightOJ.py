def lcs (s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i, w1 in enumerate(s1, 1):
        for j, w2 in enumerate(s2, 1):
            if w1 == w2:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
    return dp


def count_ways(s1, s2, dp):
    n, m = len(s1), len(s2)
    nums = [[1] * (m + 1) for _ in range(n + 1)]
    for i, w1 in enumerate(s1, 1):
        for j, w2 in enumerate(s2, 1):
            if w1 == w2:
                nums[i][j] = nums[i - 1][j - 1]
            elif dp[i][j - 1] < dp[i - 1][j]:
                nums[i][j] = nums[i][j - 1]
            elif dp[i][j - 1] > dp[i - 1][j]:
                nums[i][j] = nums[i - 1][j]
            else:
                nums[i][j] = nums[i - 1][j] + nums[i][j - 1]
    return nums[-1][-1]


if __name__ == "__main__":
    tc = int(input())
    for t in range(1, tc + 1):
        s1, s2 = input(), input()
        dp = lcs(s1, s2)
        count = count_ways(s1, s2, dp)
        print("Case %s: %s %s" % (t, dp[-1][-1], count))
