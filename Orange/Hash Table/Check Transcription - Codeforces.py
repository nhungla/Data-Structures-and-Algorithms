if __name__ == "__main__":
    s = input()
    t = input()
    count = [0] * 2
    for ch in s:
        count[int(ch)] += 1

