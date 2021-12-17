def exact_change(price, coins):
    max_coin = sum(coins)
    dp = [float("inf")] * (max_coin + 1)
    dp[0] = 0
    for coin in coins:
        for p in range(price, -1, -1):
            if dp[p] < float("inf"):
                dp[p + coin] = min(dp[p + coin], dp[p] + 1)
    for i in range(price, max_coin + 1):
        if dp[i] < float("inf"):
            return i, dp[i]


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        price = int(input())
        n = int(input())
        coins = []
        for _ in range(n):
            coins.append(int(input()))
        p, c = exact_change(price, coins)
        print(p, c)

