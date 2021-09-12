def bear_and_game(arr):
    stime = 0
    if arr[0] > 15:
        return 15
    stime += arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 15:
            return stime + 15
        stime = arr[i]

    ans = stime + 15
    return ans if ans <= 90 else 90


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(bear_and_game(arr))
