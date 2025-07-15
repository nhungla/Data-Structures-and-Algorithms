import sys
sys.setrecursionlimit(10 ** 7)


def solve(nums, idx, length, mem):
    if idx == length:
        return 1
    if nums[idx] == '0':
        return 0
    if mem[idx] != -1:
        return mem[idx]
    ans = solve(nums, idx + 1, length, mem)
    if idx + 1 < length:
        if nums[idx] == '1':
            ans += solve(nums, idx + 2, length, mem)
        elif nums[idx] == '2' and nums[idx + 1] <= '6':
            ans += solve(nums, idx + 2, length, mem)
    mem[idx] = ans
    return ans


if __name__ == "__main__":
    while True:
        ss = input()
        if ss == '0':
            break
        mem = [-1] * len(ss)
        print(solve(ss, 0, len(ss), mem))
