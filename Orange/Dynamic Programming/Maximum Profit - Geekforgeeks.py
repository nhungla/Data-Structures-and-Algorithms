def find_max_profit(prices, n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    hold = [[float("-inf")] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j, price in enumerate(prices, 1):
            dp[i][j] = max(dp[i][j - 1], hold[i][j - 1] + price)
            hold[i][j] = max(hold[i][j - 1], dp[i - 1][j - 1] - price)
    return dp[-1][-1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k, n = int(input()), int(input())
        prices = list(map(int, input().split()))
        max_profit = find_max_profit(prices, n, k)
        print(max_profit)
