if __name__ == "__main__":
    s = input()
    cur = ord('a')
    ans = 0
    for ch in s:
        tmp = abs(ord(ch) - cur)
        cur = ord(ch)
        if tmp > 12:
            tmp = 26 - tmp
        ans += tmp
    print(ans)
