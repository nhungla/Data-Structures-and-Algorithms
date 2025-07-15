import collections
import sys

sys.setrecursionlimit(10 ** 7)
NOT_VISITED = 0
PROCESSING = 1
COMPLETED = 2


def is_has_cycle(gr, cur, colors):
    colors[cur] = PROCESSING
    for ne in gr[cur]:
        if colors[ne] == NOT_VISITED:
            if not is_has_cycle(gr, ne, colors):
                return False
        elif colors[ne] == PROCESSING:
            return False
    colors[cur] = COMPLETED
    return True


def sort(cur, seen, st):
    seen.add(cur)
    for ne in gr[cur]:
        if ne not in seen:
            sort(ne, seen, st)
    st.append(cur)


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    main_courses = list(map(int, input().split()))
    main_courses = set(main_courses)
    gr = collections.defaultdict(list)
    for i in range(1, n + 1):
        tmp = list(map(int, input().split()))
        if tmp[0] == 0:
            continue
        gr[i].extend(tmp[1:])
    colors = [NOT_VISITED] * (n + 1)
    for i in range(1, n + 1):
        if colors[i] == NOT_VISITED and not is_has_cycle(gr, i, colors):
            print("-1")
            exit()
    seen, st = set(), []
    for val in main_courses:
        if val not in seen:
            sort(val, seen, st)
    for i in range(1, n + 1):
        if i not in seen:
            sort(i, seen, st)
    count, end = 0, 0
    for idx, val in enumerate(st):
        if val in main_courses:
            count += 1
        if count == len(main_courses):
            end = idx
            break
    print(idx + 1)
    print(" ".join(str(val) for val in st[:idx + 1]))

