def is_power_of_2(num):
    return (num and (num & (num - 1)) == 0)


def solve(arr, n):
    if n == 1:
        return is_power_of_2(arr[0])
    total = 0
    for i in range(32):
        total |= (1 << i)
    for i in range(32):
        ans = total
        for j in range(n):
            if arr[j] & (1 << i):
                ans &= arr[j]
        if is_power_of_2(ans):
            return True
    return False


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        arr = list(map(int, input().split()))
        print("YES" if solve(arr, n) else "NO")
