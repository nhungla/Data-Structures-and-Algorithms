def generate(s, n, count):
    if len(s) == n:
        if count == 0:
            print(s)
        return
    generate(s + '0', n, count)
    generate(s + '1', n, count - 1)


if __name__ == "__main__":
    tcs = int(input())
    for _ in range(tcs):
        input()
        n, h = list(map(int, input().split()))
        generate("", n, h)
        print()
