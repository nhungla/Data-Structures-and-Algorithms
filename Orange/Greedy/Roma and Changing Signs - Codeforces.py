if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()
    i = 0
    while k > 0:
        if i == n:
            i = 0
        if nums[i] > 0:
            break
        nums[i] *= -1
        i += 1
        k -= 1
    k %= 2
    nums.sort()
    nums[0] = -nums[0] if k else nums[0]
    print(sum(nums))
