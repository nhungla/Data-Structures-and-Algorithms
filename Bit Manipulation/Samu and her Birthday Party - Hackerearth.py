if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n, k = list(map(int, input().split()))
        # store input string
        favos = []
        selects = []
        for _ in range(n):
            favos.append(input())
        for favo in favos:
            a = 0
            for j in range(k):
                if favo[j] == '1':
                    a |= (1 << (k - 1 - j))
            selects.append(a)
        ans = k
        for i in range(1, 1 << k):
            use = True
            for j in range(n):
                if selects[j] & i == 0:
                    use = False
            if use:
                count = 0
                mask = i
                while mask:
                    if mask & 1:
                        count += 1
                    mask >>= 1
                ans = min(ans, count)
        print(ans)
