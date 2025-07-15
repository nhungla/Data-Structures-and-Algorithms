import math


def cal_distance(a, b):
    xa, ya = a
    xb, yb = b
    return math.sqrt((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb))


def find_mindist(points, start, end):
    min_dist = float("inf")
    for i in range(start, end):
        for j in range(i + 1, end):
            min_dist = min(min_dist, cal_distance(points[i], points[j]))
    return min_dist


def strip_closest(points, left, right, mid, dist_min):
    pivot = points[mid]
    splitted_points = []
    for i in range(left, right):
        if abs(points[i][0] - pivot[0]) <= dist_min:
            splitted_points.append(points[i])
    splitted_points.sort(key=lambda x: x[1])
    min_val = dist_min
    for i in range(0, len(splitted_points)):
        for j in range(i + 1, len(splitted_points)):
            if not (splitted_points[j][1] - splitted_points[i][1]) < min_val:
                break
            d = cal_distance(splitted_points[i], splitted_points[j])
            min_val = min(min_val, d)
    return min_val


def minimal_dist(points, left, right):
    if right - left <= 3:
        return find_mindist(points, left, right)
    mid = (left + right) >> 1
    d_left = minimal_dist(points, left, mid)
    d_right = minimal_dist(points, mid + 1, right)
    dist_min = min(d_left, d_right)
    return min(dist_min, strip_closest(points, left, right, mid, dist_min))


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y = list(map(int, input().split()))
            points.append((x, y))
        points.sort(key=lambda x: (x[0], x[1]))
        ans = minimal_dist(points, 0, n)
        print(format(ans, ".4f") if ans < 10000 else "INFINITY")
