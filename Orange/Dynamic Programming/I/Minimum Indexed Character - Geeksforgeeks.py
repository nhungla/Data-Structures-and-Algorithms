if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        patt = input()
        map_idx = {}
        for i in range(len(s) - 1, -1, -1):
            map_idx[s[i]] = i
        min_idx = float("inf")
        for ch in patt:
            min_idx = min(min_idx, map_idx.get(ch, float("inf")))
        print(s[min_idx] if min_idx < float("inf") else "No character present")
