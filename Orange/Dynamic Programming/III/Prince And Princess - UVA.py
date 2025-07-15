def lis(nums):
    st = []
    for val in nums:
        if not st or st[-1] <= val:
            st.append(val)
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
    testcase = int(input())
    for t in range(1, testcase + 1):
        n, p, q = list(map(int, input().split()))
        prince = list(map(int, input().split()))
        princess = list(map(int, input().split()))
        pos = [-1] * (n * n + 1)
        arr = []
        for idx, val in enumerate(prince):
            pos[val] = idx
        for val in princess:
            if pos[val] != -1:
                arr.append(pos[val])
        ans = lis(arr)
        print("Case %s: %s" % (t, ans))
