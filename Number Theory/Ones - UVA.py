if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            r = count = 1
            while r % n != 0:
                r = (r * 10 + 1) % n
                count += 1
            print(count)
        except:
            break
            pass
