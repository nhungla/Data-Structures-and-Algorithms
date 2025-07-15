import collections


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = collections.defaultdict(lambda: 0)
    for i, w1 in enumerate(s1):
        for j, w2 in enumerate(s2):
            if w1 == w2:
                dp[i, j] = 1 + dp[i - 1, j - 1]
            else:
                dp[i, j] = max(dp[i, j - 1], dp[i - 1, j])
    count = dp[n - 1, m - 1]
    ans = []
    x, y = n - 1, m - 1
    while count:
        if dp[x - 1, y] < dp[x, y] and dp[x, y - 1] < dp[x, y]:
            ans.append(s1[x])
            count -= 1
        if dp[x - 1, y] > dp[x, y - 1]:
            x -= 1
        else:
            y -= 1
    return ans


if __name__ == "__main__":
    try:
        while True:
            s1, s2 = [], []
            while True:
                tmp = input()
                if tmp == "#":
                    break
                s1.extend(tmp.split())
            while True:
                tmp = input()
                if tmp == "#":
                    break
                s2.extend(tmp.split())
            ans = lcs(s1, s2)
            print(' '.join(ans[::-1]))
    except:
        pass
