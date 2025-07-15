def backtrack(nums, ans, tmp, start, k):
    if len(tmp) == 6:
        ans.append(list(tmp))
        return
    for i, val in enumerate(nums[start:], start):
        tmp.append(val)
        backtrack(nums, ans, tmp, i + 1, k)
        tmp.pop()


if __name__ == "__main__":
    while True:
        arr = list(map(int, input().split()))
        if arr[0] == 0:
            break
        k, nums = arr[0], arr[1:]
        nums.sort()
        ans = []
        backtrack(nums, ans, [], 0, k)
        ans.sort()
        for val in ans:
            print(" ".join(str(v) for v in val))
        print()
