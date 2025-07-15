def lis(nums):
    import bisect
    n = len(nums)
    dp = [1] * n
    sub = [nums[0]]
    for i in range(1, n):
        pos = bisect.bisect_left(sub, nums[i])
        if pos == len(sub):
            sub.append(nums[i])
        else:
            sub[pos] = nums[i]
        dp[i] = pos + 1
    return dp


if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            nums = list(map(int, input().split()))
        except:
            break
        dp = lis(nums)
        re_dp = lis(nums[::-1])
        max_len = 1
        for i in range(n):
            min_len = min(dp[i], re_dp[n - i - 1])
            max_len = max(max_len, min_len * 2 - 1)
        print(max_len)
