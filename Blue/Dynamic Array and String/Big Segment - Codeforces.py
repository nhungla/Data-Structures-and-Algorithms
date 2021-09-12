if __name__ == "__main__":
    n = int(input())
    l_arr, r_arr = [], []
    for i in range(n):
        tmp = list(map(int, input().split()))
        l_arr.append(tmp[0])
        r_arr.append(tmp[1])
    left, right = min(l_arr), max(r_arr)
    idx = 0
    for (x, y) in zip(l_arr, r_arr):
        if x == left and y == right:
            break
        idx += 1
    print(idx + 1 if idx < n else -1)
