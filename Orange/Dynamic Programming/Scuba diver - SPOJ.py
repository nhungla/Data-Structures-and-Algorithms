import sys
sys.setrecursionlimit(10**6)


def solve(idx, dp, oxis, nitos, weights, vo, vn):
    if dp[idx][vo][vn] != -1:
        return dp[idx][vo][vn]
    if vo == 0 and vn == 0:
        dp[idx][vo][vn] = 0
        return dp[idx][vo][vn]
    if idx == 0:
        dp[idx][vo][vn] = float("inf")
    else:
        not_take = solve(idx - 1, dp, oxis, nitos, weights, vo, vn)
        new_o = max(vo - oxis[idx],  0)
        new_n = max(vn - nitos[idx], 0)
        take = solve(idx - 1, dp, oxis, nitos, weights, new_o, new_n) + weights[idx]
        dp[idx][vo][vn] = min(not_take, take)
    return dp[idx][vo][vn]


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        vo, vn = list(map(int, input().split()))
        n = int(input())
        oxis = [0 for _ in range(n + 1)]
        nitos = [0 for _ in range(n + 1)]
        weights = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            oxis[i], nitos[i], weights[i] = list(map(int, input().split()))
        dp = [[[-1] * (vn + 1) for _ in range(vo + 1)] for _ in range(n + 1)]
        solve(n, dp, oxis, nitos, weights, vo, vn)
        print(dp[n][vo][vn])
        try:
            input()
        except:
            pass
