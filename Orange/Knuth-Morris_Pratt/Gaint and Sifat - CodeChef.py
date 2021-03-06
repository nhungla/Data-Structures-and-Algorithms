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
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix[i] = 0
                i += 1
    return prefix


def kmp_count(text, pattern):
    prefix = build_prefix(pattern)
    i = j = 0
    count = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i, j = i + 1, j + 1
        if j == len(pattern):
            count += 1
            j = prefix[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return count


if __name__ == "__main__":
    testcase = int(input())
    for tc in range(1, testcase + 1):
        s, t = input().replace(' ', ''), input().replace(' ', '')
        ans = kmp_count(s, t)
        print("Case %s: %s" % (tc, ans))
