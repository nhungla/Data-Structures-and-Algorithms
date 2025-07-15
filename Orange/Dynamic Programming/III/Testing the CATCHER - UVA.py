def lis(nums):
    st = []
    for val in nums:
        if not st or st[-1] <= val:
            st.append(val)
        else:
            l, r = -1, len(st) - 1
            while l + 1 < r:
                m = (l + r) >> 1
                if st[m] > val:
                    r = m
                else:
                    l = m
            if st[r] > val:
                st[r] = val
    return len(st)


if __name__ == "__main__":
    tc = 1
    while True:
        nums = []
        while True:
            num = int(input())
            if num == -1:
                break
            nums.append(num)
        if not nums:
            break
        print("Test #%s:" % tc)
        print("  maximum possible interceptions: %s" % lis(nums[::-1]))
        print()
        tc += 1
