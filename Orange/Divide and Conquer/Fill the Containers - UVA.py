def can_fill(capacity, a, m):
    container = 0
    numberOfContainer = 0
    for i in range(len(a)):
        if a[i] > capacity:
            return False
        if container + a[i] > capacity:
            container = 0
        if container == 0:
            numberOfContainer += 1
        if numberOfContainer > m:
            return False
        container += a[i]
    return True


def binarySearch(a, total, m):
    left = -1
    right = total
    while left + 1 < right:
        mid = (left + right) >> 1
        if can_fill(mid, a, m):
            right = mid
        else:
            left = mid
    return right


if __name__ == "__main__":
    while True:
        try:
            n, m = map(int, input().split())
            c = list(map(int, input().split()))
            total = sum(c)
            print(binarySearch(c, total, m))
        except EOFError:
            break
