if __name__ == "__main__":
    s = list(input())
    t = list(input())
    n = len(s)
    for i in range(n - 1, -1, -1):
        if s[i] == 'z':
            s[i] = 'a'
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    print(''.join(s) if s != t else 'No such string')
