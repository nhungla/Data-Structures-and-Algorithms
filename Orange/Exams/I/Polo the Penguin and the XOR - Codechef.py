def to_bin(num):
    s = bin(num)[2:]
    return set(len(s) - i - 1 for i in range(len(s)) if s[i] == '1')


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        nums = list(map(int, input().split()))
        max_len = len(bin(max(nums))) - 2
        max_len = len(bin(max(nums))[2:])
        arr = [0] * max_len
        ss = 0
        total = 0
        for idx, val in enumerate(nums):
            ss ^= val
            bin_s = to_bin(ss)
            for j in range(len(arr)):
                if j in bin_s:
                    total += (idx + 1 - arr[j]) * (2 ** j)
                    arr[j] += 1
                else:
                    total += arr[j] * (2 ** j)
        print(total)
