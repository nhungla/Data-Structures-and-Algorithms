t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]
    for i in range(n):
        a.append(int(input()))
    Fa = [1] * (n + 1)
    Fb = [1] * (n + 1)
    ans = 0
    for i in range(n, 0, -1):
        for j in range(i + 1, n + 1):
            if a[j] < a[i]:
                Fa[i] = max(Fa[i], Fa[j] + 1)
            if a[j] > a[i]:
                Fb[i] = max(Fb[i], Fb[j] + 1)
        ans = max(ans, Fa[i] + Fb[i] - 1)
    print(ans)
