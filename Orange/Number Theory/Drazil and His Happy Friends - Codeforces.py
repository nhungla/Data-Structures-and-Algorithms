if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    boys = [False] * n
    girls = [False] * m
    arr = list(map(int, input().split()))
    if len(arr) > 1:
        for val in arr[1:]:
            boys[val] = True
    arr = list(map(int, input().split()))
    if len(arr) > 1:
        for val in arr[1:]:
            girls[val] = True
    day = 0
    while day < n * m:
        b = day % n
        g = day % m
        if boys[b] or girls[g]:
            boys[b] = girls[g] = True
        day += 1
    ans = 0
    for b in boys:
        if not b:
            print("No")
            exit()
    for g in girls:
        if not g:
            print("No")
            exit()
    print("Yes")
