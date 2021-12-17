import collections

if __name__ == "__main__":
    s = input()
    t = input()
    counter_t = collections.Counter(t)
    used = [False] * len(s)
    # print(s)
    yay = whoops = 0
    for idx, ch in enumerate(s):
        if counter_t[ch] > 0:
            counter_t[ch] -= 1
            yay += 1
            used[idx] = True
    for idx, ch in enumerate(s):
        if used[idx]:
            continue
        if ch.islower() and counter_t[ch.upper()] > 0:
            counter_t[ch.upper()] -= 1
            whoops += 1
        elif ch.isupper() and counter_t[ch.lower()] > 0:
            counter_t[ch.lower()] -= 1
            whoops += 1
    print("%s %s" % (yay, whoops))
