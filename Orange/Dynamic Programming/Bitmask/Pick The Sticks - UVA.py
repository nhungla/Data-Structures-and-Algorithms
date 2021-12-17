""""
*2 độ dài thanh vàng và container
dp[i][j][k] là độ dài lớn nhất thanh vàng i (1 ->), chiều dài container = j và k số thanh nằm ở đầu (0 <= k <= 2)

dp[i][j][k] = max{
            dp[i - 1][j][k] (bỏ qua thanh i)
            dp[i - 1][j - 2 * a[i]][k] + v[i] if j >= 2 * a[i] (thêm thanh vàng i vào)
            dp[i - 1][j - a[i]][k - 1] + v[i] if j >= a[i] and k > 0 (thêm vào nhưng chỉ chứa 1/2)
            }
base case:
    dp[0][j][0] = dp[i][0][k] = 0
    dp[0][j][k] = float("-inf")

Time complexity: O(n * l) (n: số lượng thanh vàng, l độ dài container)
"""
def solve(golds, l, n):
    dp = [[[0] * 3 for _ in range(2 * l + 1)] for _ in range(n + 1)]
    for i, (a, v) in enumerate(golds[1:], 1):
        for j in range(1, 2 * l + 1):
            for k in range(3):
                dp[i][j][k] = dp[i - 1][j][k]
                if j >= 2 * a:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 2 * a][k] + v)
                if j >= a and k:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - a][k - 1] + v)
    return dp


if __name__ == "__main__":
    testcase = int(input())
    for t in range(1, testcase + 1):
        input()
        n, l = list(map(int, input().split()))
        golds = [(0, 0)]
        ans = -1
        for _ in range(n):
            a, v = list(map(int, input().split()))
            golds.append((a, v))
            ans = max(ans, v)
        dp = solve(golds, l, n)
        for k in range(3):
            ans = max(ans, dp[-1][-1][k])
        print("Case #%s: %s" % (t, ans))
