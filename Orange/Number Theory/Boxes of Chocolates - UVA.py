if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, b = list(map(int, input().split()))
        ans = 0
        for _ in range(b):
            arr = list(map(int, input().split()))
            tmp = 1
            for val in arr[1:]:
                tmp *= val
                tmp %= n
            ans += tmp
            ans %= n
        print(ans)
