from functools import lru_cache


@lru_cache(None)
def coin_change(n):
    if n == 0:
        return 0
    tmp = coin_change(n // 2) + coin_change(n // 3) + coin_change(n // 4)
    return max(n, tmp)


if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            ans = coin_change(n)
            print(ans)
        except:
            break
