if __name__ == "__main__":
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    vests = []
    i = j = 0

    while i < n and j < m:
        if a[i] - x <= b[j] <= a[i] + y:
            vests.append((i + 1, j + 1))
            i, j = i + 1, j + 1
        elif a[i] + y < b[j]:
            i += 1
        elif a[i] - x > b[j]:
            j += 1
    print(len(vests))
    for u, v in vests:
        print(u, v)
