def kmp(text):
    n = len(text)
    prefix = [0] * n
    prefix[0] = now = -1
    for i in range(1, n):
        while now != -1 and text[i] != text[now + 1]:
            now = prefix[now]
        if text[i] == text[now + 1]:
            now += 1
            prefix[i] = now
        else:
            prefix[i] = -1
    return prefix


if __name__ == "__main__":
    text = input()
    prefix = kmp(text)
    n = len(text)
    max_val = prefix[n - 1]
    found = prefix[max_val] if max_val != -1 else -1
    for i in range(1, n - 1):
        if prefix[i] == max_val:
            found = max_val
    print('Just a legend' if found == -1 else text[:found + 1])
