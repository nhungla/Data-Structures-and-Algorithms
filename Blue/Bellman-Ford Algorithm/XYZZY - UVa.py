import collections


def bellman(gr, n):
    costs = [0] * n
    costs[0] = 100
    inqueue = [False] * n
    inqueue[0] = True
    queue = collections.deque([0])
    cnt = [0] * n
    while queue:
        cur = queue.popleft()
        inqueue[cur] = False
        for ne, c in gr[cur]:
            if costs[cur] + c > costs[ne] and cnt[ne] <= 7000:
                costs[ne] = costs[cur] + c
                cnt[ne] += 1
                if not inqueue[ne]:
                    queue.append(ne)
                    inqueue[ne] = True
    return costs[n - 1] > 0


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == -1:
            break
        gr = collections.defaultdict(list)
        for i in range(n):
            arr = list(map(int, input().split()))
            room = arr[1]
            for v in arr[2:]:
                gr[i].append((v - 1, arr[0]))
        costs = []
        is_win = bellman(gr, n)
        print("winnable") if is_win else print("hopeless")