def num_to_arr(n):
    ans = []
    while n:
        ans.append(n % 10)
        n //= 10
    return ans[::-1]


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        nums = num_to_arr(n)
        len_nums = len(nums)
        l = sum(nums)
        left, right = 0, l - 1
        ans = True
        while left < right:
            if nums[left % len_nums] != nums[right % len_nums]:
                ans = False
                break
            left, right = left + 1, right - 1
        print("YES" if ans else "NO")
