def count(arr):
    if len(arr) == 2:
        return 1, 1
    l, r = 0, len(arr) - 1
    a, b = 0, 0
    while l < r:
        if a > b:
            b += arr[r]
            r -= 1
        elif a < b:
            a += arr[l]
            l += 1
        else:
            a, b = arr[l], arr[r]
            l, r = l + 1, r - 1
    if a <= b:
        alice, bob = l + 1, len(arr) - r - 1
    else:
        alice, bob = l, len(arr) - r
    return alice, bob


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    a, b = count(arr)
    print(a, b)
