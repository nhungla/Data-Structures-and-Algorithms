def solve(n):
    dummy = result = n
    count = 0
    ans = -1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            ans = max(ans, i)
            count += 1
    if ans == -1:
        return -1
    if n != 1 and ans != n:
        count += 1
    return -1 if count <= 1 else max(ans, n)


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        print(solve(abs(n)))
