import sys

sys.setrecursionlimit(10 ** 7)


def helper(fences, l, r, h):
    if l >= r:
        return 0
    min_idx = l
    for i in range(l, r):
        if fences[min_idx] > fences[i]:
            min_idx = i
    return min(r - l, fences[min_idx] - h + helper(fences, l, min_idx, fences[min_idx]) + helper(fences, min_idx + 1, r,
                                                                                                 fences[min_idx]))


if __name__ == "__main__":
    n = int(input())
    fences = list(map(int, input().split()))
    ans = helper(fences, 0, n, 0)
    print(ans)
