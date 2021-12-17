import collections

if __name__ == "__main__":
    n = int(input())
    gr = collections.defaultdict(list)
    for _ in range(n):
        a, b, c = input().split()
        gr[a].append(b)
        gr[a].append(c)
        gr[b].append(a)
        gr[b].append(c)
        gr[c].append(a)
        gr[c].append(b)
    mm = {"Isenbaev": 0}
    pool = ["Isenbaev"]
    count = 0
    while pool:
        tmp = []
        count += 1
        for cur in pool:
            for ch in gr[cur]:
                if ch in mm:
                    continue
                mm[ch] = count
                tmp.append(ch)
        pool = tmp
    for k in gr.keys():
        if k not in mm:
            mm[k] = "undefined"
    ans = list(mm.keys())
    ans.sort()
    for v in ans:
        print("%s %s" % (v, mm[v]))
