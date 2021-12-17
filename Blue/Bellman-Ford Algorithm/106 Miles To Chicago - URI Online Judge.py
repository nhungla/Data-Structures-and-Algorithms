def bellman(gr, start, n):
    probs = [0] * n
    probs[start] = 100.0
    for i in range(n):
        for u, v, c in gr:
            p = (probs[u] * c) / 100.0
            if probs[v] < p:
                probs[v] = p
    return probs[n - 1]


if __name__ == "__main__":
    while True:
        inp = input()
        if len(inp) == 1:
            break
        n, m = list(map(int, inp.split()))
        gr = []
        for i in range(m):
            u, v, c = list(map(int, input().split()))
            gr.append((u - 1, v - 1, c))
            gr.append((v - 1, u - 1, c))
        ans = bellman(gr, 0, n)
        print(format(ans, ".6f"), "percent")
