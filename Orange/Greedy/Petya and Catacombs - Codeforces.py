if __name__ == "__main__":
    n = int(input())
    tmp = list(map(int, input().split()))

    t = [0] * (n + 1)
    for x in tmp:
        t[x] = 1
    count = 1
    for val in t[:-1]:
        if not val:
            count += 1
    print(count)
