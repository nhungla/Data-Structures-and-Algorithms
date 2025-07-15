def solve(s):
    k = 0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        while k > 0 and s[k] != s[i]:
            k = dp[k - 1]
        if s[k] == s[i]:
            k += 1
        dp[i] = k
    return dp


if __name__ == "__main__":
    while True:
        k, s = list(input().split())
        k = int(k)
        if k == -1:
            break
        dp = solve(s)
        n = len(s)
        ans = (k - dp[n - 1]) // (n - dp[n - 1]) if k >= n else 0
        print(ans)
