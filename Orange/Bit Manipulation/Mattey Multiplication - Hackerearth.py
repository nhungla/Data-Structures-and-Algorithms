if __name__ == "__main__":
    tcs = int(input())
    for _ in range(tcs):
        n, m = list(map(int, input().split()))
        ans = []
        idx = 0
        while m != 0:
            if m & 1:
                ans.append(idx)
            m = m >> 1
            idx += 1
        ss = ""
        for i in range(len(ans) - 1, -1, -1):
            ss += " + (" + str(n) + "<<" + str(ans[i]) + ")"
        print(ss[3:])
