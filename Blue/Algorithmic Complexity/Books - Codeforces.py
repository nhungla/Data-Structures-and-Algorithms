def countBooks(arr, limit):
    total = 0
    start = 0
    ans = 0
    for end, val in enumerate(arr):
        total += val
        if total > limit:
            total -= arr[start]
            start += 1
        ans = max(ans, end - start + 1)
    return ans


if __name__ == "__main__":
    ns = list(map(int, input().split()))
    k = ns[1]
    arr = list(map(int, input().split()))
    print(countBooks(arr, k))
