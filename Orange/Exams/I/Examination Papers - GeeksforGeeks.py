MOD = 10 ** 9 + 7


def po(x, y):
    if y == 0:
        return 1
    tmp = po(x, y >> 1)
    if y & 1:
        return (x * tmp * tmp) % MOD
    return (tmp * tmp) % MOD


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print((po(2, n) - 1 + MOD) % MOD)
