T = int(input())

for _ in range(T):
    n = int(input())

    S = list(map(int, input().split()))
    F = list(map(int, input().split()))

    a = [(F[i], S[i], i) for i in range(n)]

    a.sort()

    i = 0
    prev = -1
    ans = []
    while i < n:
        if a[i][1] > prev:
            ans.append(a[i][2] + 1)
            prev = a[i][0]
        i += 1

    print(' '.join(map(str, ans)))