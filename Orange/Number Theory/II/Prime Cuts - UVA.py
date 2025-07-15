def solve(n):
    mark = [True] * (n + 1)
    primes = [1]
    mark[0] = mark[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if mark[i]:
            for j in range(i * i, n + 1, i):
                mark[j] = False
    for i in range(2, n + 1):
        if mark[i]:
            primes.append(i)
    return primes


if __name__ == "__main__":
    while True:
        try:
            n, c = list(map(int, input().split()))
            primes = solve(n)
            l = len(primes)
            start, end = 0, l - 1
            if l & 1 and 2 * c - 1 < l:
                mid = (l - 1) >> 1
                start = mid - (c - 1)
                end = mid + (c - 1)
            elif not (l & 1) and 2 * c < l:
                mid = l >> 1
                start = mid - (2 * c + 1) // 2
                end = mid + c - 1
            ans = ' '.join(str(val) for val in primes[start: end + 1])
            print("%s %s: %s" % (n, c, ans))
            print()
        except:
            break
            pass
