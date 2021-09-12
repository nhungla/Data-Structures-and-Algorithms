def build_prefix(p):
    m = len(p)
    prefix = [0] * m
    i, j = 1, 0
    while i < m:
        if p[i] == p[j]:
            j += 1
            prefix[i] = j
            i += 1
        else:
            if j != 
if __name__ == "__main__":
    testcase = int(input())
    for t in range(1, testcase + 1):
        s, t = input().replace(' ', ''), input().replace(' ', '')

