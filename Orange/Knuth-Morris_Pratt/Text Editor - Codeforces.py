def build_prefix(text):
    m = len(text)
    prefix = [0] * m
    i, j = 1, 0
    while i < m:
        if text[i] == text[j]:
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


def search(text, pattern, count):
    prefix = build_prefix(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i, j = i + 1, j + 1
        if j == len(pattern):
            count -= 1
            if count == 0:
                return True
            j = prefix[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return True if count == 0 else False


if __name__ == "__main__":
    text, pattern, count = input().replace(' ', ''), input().replace(' ', ''), int(input())
    while pattern:
        if search(text, pattern, count):
            print(pattern)
            exit()
        pattern = pattern[:-1]
    print("IMPOSSIBLE")
