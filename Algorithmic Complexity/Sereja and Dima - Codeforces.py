def totalPoint(arr):
    l, r = 0, len(arr) - 1
    se, di = 0, 0
    check = True
    while l <= r:
        if arr[l] > arr[r]:
            tmp = arr[l]
            l += 1
        else:
            tmp = arr[r]
            r -= 1
        if check:
            se += tmp
            check = False
        else:
            di += tmp
            check = True
    return se, di


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    se, di = totalPoint(arr)
    print(se, di)
