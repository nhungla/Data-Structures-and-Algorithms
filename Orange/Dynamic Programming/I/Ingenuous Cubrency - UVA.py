if __name__ == "__main__":
    dp = [0] * 10000
    dp[0] = 1
    for i in range(1, 22):
        for j in range(i * i * i, 10000):
            dp[j] += dp[j - i * i * i]
    while True:
        try:
            n = int(input())
        except:
            break
    print(dp[n])
