import collections


def lcs(s1, s2, s3):
    n, m, p = len(s1), len(s2), len(s3)
    dp = collections.defaultdict(lambda: 0)
    for i, w1 in enumerate(s1):
        for j, w2 in enumerate(s2):
            for k, w3 in enumerate(s3):
                if w1 == w2 == w3:
                    dp[i, j, k] = 1 + dp[i - 1, j - 1, k - 1]
                else:
                    dp[i, j, k] = max(dp[i - 1, j, k], dp[i, j - 1, k], dp[i, j, k - 1])
    return dp[n - 1, m - 1, p - 1]


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        lens = list(map(int, input().split()))
        strings = list(input().split())
        print(lcs(strings[0], strings[1], strings[2]))
