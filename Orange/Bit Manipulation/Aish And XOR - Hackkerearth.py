if __name__ == "__main__":
    n = int(input())
    bits = list(map(int, input().split()))
    q = int(input())
    xor = [0] * n
    counts = [0] * n
    xor[0] = bits[0]
    counts[0] = int(bits[0] == 0)
    for idx, val in enumerate(bits[1:], 1):
        xor[idx] = xor[idx - 1] ^ val
        counts[idx] = counts[idx - 1] + int(val == 0)
    # print(xor)
    for _ in range(q):
        l, r = list(map(int, input().split()))
        l, r = l - 1, r - 1
        ans = xor[r] ^ xor[l - 1] if l else xor[r]
        count = counts[r] - counts[l - 1] if l else counts[r]
        print("%s %s" % (ans, count))
