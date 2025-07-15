def solve(n_list, k):
    ss = sum(n_list)
    ans = 0
    idx = 0
    while ss < k:
        ss = ss - n_list[idx] + 9
        idx += 1
        ans += 1
    return ans


if __name__ == "__main__":
    k = int(input())
    n = int(input())
    arr = []
    while n > 0:
        arr.append(n % 10)
        n //= 10
    arr.sort()
    print(solve(arr, k))
