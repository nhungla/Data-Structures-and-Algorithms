n = int(input())

a = []
d1 = [0 for _ in range(2 * n)]
d2 = [0 for _ in range(2 * n)]
for i in range(n):
    a.append(list(map(int, input().split(' '))))
    for j in range(n):
        d1[i + j] += a[i][j]
        d2[i - j + n] += a[i][j]

res = [-1, -1]
x = [-1, -1]
y = [-1, -1]

for i in range(n):
    for j in range(n):
        pos = (i + j) & 1
        tot = d1[i + j] + d2[i - j + n] - a[i][j]
        if tot > res[pos]:
            res[pos] = tot
            x[pos] = i + 1
            y[pos] = j + 1

print(sum(res))
print(x[0], y[0], x[1], y[1])