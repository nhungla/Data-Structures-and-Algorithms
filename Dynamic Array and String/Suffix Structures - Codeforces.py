import collections


# 0: need tree; 1: automaton; 2: array; 3: both
def solution(s, t):
    s_counter, t_counter = collections.Counter(s), collections.Counter(t)
    array, auto = False, False
    if len(s_counter) < len(t_counter):
        return 0
    for val in t_counter:
        if s_counter[val] < t_counter[val]:
            return 0
        if s_counter[val] > t_counter[val]:
            auto = True
    if len(s_counter) > len(t_counter):
        auto = True
    idx, order = 0, -1
    for i, val in enumerate(t):
        idx = s.find(val, order + 1)
        if idx > order:
            order = idx
        else:
            array = True
            break

    if auto and array:
        return 3
    if auto:
        return 1
    if array:
        return 2


if __name__ == "__main__":
    s = list(map(str, input().split()))
    s = ''.join(s)
    t = list(map(str, input().split()))
    t = ''.join(t)

    ans = solution(s, t)
    if ans == 0:
        print('need tree')
    elif ans == 3:
        print('both')
    elif ans == 2:
        print('array')
    else:
        print('automaton')
