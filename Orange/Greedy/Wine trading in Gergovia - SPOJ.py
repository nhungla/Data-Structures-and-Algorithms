if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        wine = list(map(int, input().split()))
        ss = ans = 0
        for w in wine:
            ss += w
            ans += abs(ss)
        print(ans)
