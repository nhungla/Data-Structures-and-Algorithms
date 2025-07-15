def find_phi(n):
    re = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            re = re // i * (i - 1)
    if n > 1:
        re = re // n * (n - 1)
    return re


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        print(find_phi(n))
