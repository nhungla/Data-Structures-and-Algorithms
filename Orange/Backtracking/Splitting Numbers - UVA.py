if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        a = b = 0
        count = 1
        si = 1
        while n:
            if n & 1:
                if si > 0:
                    a += count
                else:
                    b += count
                si *= -1
            count <<= 1
            n >>= 1
        print("%s %s" % (a, b))
