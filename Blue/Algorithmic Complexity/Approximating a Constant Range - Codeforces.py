n = int(input())
a = list(map(int, input().split()))

fre = [0] * (10 ** 5 + 5)
diff = 0
j = 0
longest_range = 0

for i in range(n):
    if fre[a[i]] == 0:
        diff += 1
    fre[a[i]] += 1

    while j < n and diff > 2:
        if fre[a[j]] == 1:
            diff -= 1
        fre[a[j]] -= 1
        j += 1

    longest_range = max(longest_range, i - j + 1)

print(longest_range)