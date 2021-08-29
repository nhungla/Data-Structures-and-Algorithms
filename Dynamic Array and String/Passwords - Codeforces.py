if __name__ == '__main__':
    nums = list(map(int, input().split()))
    n, k = nums[0], nums[1]
    passwords = []

    for i in range(n):
        s = ''.join(input().split())
        passwords.append(s)
    pw = ''.join(input().split())
    len_pw = len(pw)
    low, high = 0, 0

    for p in passwords:
        if len(p) < len_pw:
            low, high = low + 1, high + 1
        elif len(p) == len_pw:
            high += 1

    high -= 1
    low = low + 1 + (low // k) * 5
    high = high + 1 + (high // k) * 5
    print(low, high)
