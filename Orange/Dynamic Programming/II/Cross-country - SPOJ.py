import collections


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = collections.defaultdict(lambda: 0)
    for i, w1 in enumerate(s1):
        for j, w2 in enumerate(s2):
            if w1 == w2:
                dp[i, j] = 1 + dp[i - 1, j - 1]
            else:
                dp[i, j] = max(dp[i - 1, j], dp[i, j - 1])
    return dp[n - 1, m - 1]


if __name__ == "__main__":
    tc = int(input().replace(" ", ""))
    for _ in range(tc):
        s1 = input().split()
        max_val = 0
        while True:
            s2 = input()
            if s2 == '0':
                break
            s2 = s2.split()
            max_val = max(max_val, lcs(s1, s2) - 1)
        print(max_val)
