class Member:
    def __init__(self, s, b, idx):
        self.s = s
        self.b = b
        self.idx = idx

    def __lt__(self, other):
        if self.s == other.s:
            return self.b > other.b
        return self.s < self.s


def lis(people, n):
    st = []
    ans = []
    for p in people:
        if not st or st[-1].b <= p.b:
            st.append(p)
            ans = list(st)
        else:
            l, r = -1, len(st) - 1
            while l + 1 < r:
                m = (l + r) >> 1
                if people[m].b >= p.b:
                    r = m
                else:
                    l = m
            if people[r].b >= p.b:
                st[r] = p
    return [pe.idx for pe in ans]


if __name__ == "__main__":
    n = int(input())
    people = []
    for i in range(n):
        si, bi = list(map(int, input().split()))
        people.append(Member(si, bi, i))
    people.sort()
    ans = lis(people, n)
    print(len(ans))
    print(' '.join(str(val + 1) for val in ans))
