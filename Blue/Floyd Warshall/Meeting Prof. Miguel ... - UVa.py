INF = 10 ** 9
MAX = 28


def FloydWarshall(dist):
    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


while True:
    N = int(input())
    if N == 0:
        break

    distS = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]
    distD = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]

    for _ in range(N):
        age, dir, x, y, c = input().split()
        u, v = map(lambda char: ord(char) - ord('A'), (x, y))
        c = int(c)

        if age == 'Y':
            distS[u][v] = min(distS[u][v], c)
            if dir == 'B':
                distS[v][u] = min(distS[v][u], c)
        else:
            distD[u][v] = min(distD[u][v], c)
            if dir == 'B':
                distD[v][u] = min(distD[v][u], c)

    s, d = map(lambda char: ord(char) - ord('A'), input().split())
    FloydWarshall(distS)
    FloydWarshall(distD)

    res = []
    minDist = INF

    for i in range(MAX):
        dist1 = distS[s][i]
        dist2 = distD[d][i]

        if dist1 != INF and dist2 != INF and dist1 + dist2 <= minDist:
            res.append((dist1 + dist2, i))
            minDist = dist1 + dist2

    if not res:
        print('You will never meet.')
    else:
        res.sort()
        print(minDist, end='')

        for place in res:
            if place[0] != minDist:
                break
            print(' ' + chr(place[1] + ord('A')), end='')
        print()