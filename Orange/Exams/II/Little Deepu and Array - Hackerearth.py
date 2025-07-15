import math


class pair:
    def __init__(self, a, b):
        self.first = a;
        self.second = b;


def func(x):
    return a.first


n = 0
arr = []


def buildTree(tree, left, right, index):
    global arr
    if left > right:
        return
    if left == right:
        tree[index] = arr[left];
        return

    buildTree(tree, left, int((left + right) / 2), index * 2)
    buildTree(tree, int((left + right) / 2) + 1, right, 2 * index + 1)
    tree[index] = min(tree[2 * index], tree[2 * index + 1])


def updateTree(tree, lazy, left, right, beg, end, index, x, val):
    if left > right or left > end or right < beg:
        return
    if lazy[index] != 0:
        tree[index] += lazy[index]
        if left != right:
            lazy[index * 2] += lazy[index]
            lazy[index * 2 + 1] += lazy[index]
        lazy[index] = 0

    if tree[index] > x:
        tree[index] += val
        if left != right:
            lazy[index * 2] += val
            lazy[index * 2 + 1] += val
        return

    if left == right:
        return
    updateTree(tree, lazy, left, int((right + left) / 2), beg, end, index * 2, x, val)
    updateTree(tree, lazy, int((left + right) / 2) + 1, right, beg, end, index * 2 + 1, x, val)
    tree[index] = min(tree[index * 2], tree[index * 2 + 1])


def queryTree(tree, lazy, left, right, beg, end, index):
    if (left > right or left > end or right < beg):
        return 100000000
    if lazy[index] != 0:
        tree[index] += lazy[index]
        if left != right:
            lazy[index * 2] += lazy[index]
            lazy[index * 2 + 1] += lazy[index]
        lazy[index] = 0

    if left >= beg and end <= right:
        return tree[index]
    q1 = queryTree(tree, lazy, left, int((left + right) / 2), beg, end, index * 2)
    q2 = queryTree(tree, lazy, int((left + right) / 2) + 1, right, beg, end, index * 2 + 1)
    res = min(q1, q2)
    return res


def main():
    global n, arr
    n = int(input())
    arr = list(map(int, input().split()))
    a = [pair(arr[i], i + 1) for i in range(n)]
    arr.sort()
    a.sort(key=lambda x: x.first)
    h = int(math.ceil(math.log(n, 2)))
    sizeTree = 2 * int(2 ** h) - 1
    segmentTree = [0] * sizeTree
    lazy = [0] * sizeTree

    buildTree(segmentTree, 0, n - 1, 1)
    numOfquery = int(input())

    for _ in range(numOfquery):
        x = int(input())
        updateTree(segmentTree, lazy, 0, n - 1, 0, n - 1, 1, x, -1)

    for i in range(n):
        a[i].first = queryTree(segmentTree, lazy, 0, n - 1, i, i, 1)
        temp = a[i].first
        a[i].first = a[i].second
        a[i].second = temp
    a.sort(key=lambda x: x.first)
    for i in range(n):
        print("{}".format(a[i].second), end=" ")


if __name__ == "__main__":
    main()