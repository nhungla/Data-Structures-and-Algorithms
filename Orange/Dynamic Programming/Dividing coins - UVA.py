if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        m = int(input())
        coins = list(map(int, input().split()))
        amount = sum(coins)
        dp = [False] * (amount + 1)
        dp[0] = True
        for val in coins:
            for am in range(amount, val - 1, -1):
                dp[am] |= dp[am - val]
        diff = -1
        for val in range(amount >> 1, -1, -1):
            if dp[val]:
                diff = abs(amount - 2 * val)
                break
        print(diff)

#Time complexity: O(m∗testcase∗(amount−min(a))
