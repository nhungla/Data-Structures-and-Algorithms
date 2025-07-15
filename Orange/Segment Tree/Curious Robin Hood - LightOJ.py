# class SegmentTree:
#     def __init__(self, nums):
#         self.nums = nums
#         self.n = len(nums)
#         self.tree = [0] * (4 * self.n)
#         self.lazy = [0] * (4 * self.n)
#
#         self.build_tree(0, 0, self.n - 1)
#
#     def build_tree(self, idx, left, right):
#         if left == right:
#             self.tree[idx] = self.nums[left]
#             return
#         mid = (left + right) >> 1
#         self.build_tree(2 * idx, left, mid)
#         self.build_tree(2 * idx + 1, mid + 1, right)
#         self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
#
#     def push_down(self, idx):
#         if self.lazy[idx] == 0:
#             return
#         left, right = idx << 1, (idx << 1) + 1
#         self.lazy[left] = self.lazy[right] = self.lazy[idx]
#         self.tree[left] = self.tree[right] = self.lazy[idx]
#         self.lazy[idx] = 0
#
#     def update(self, idx, left, right, tl, tr, value):
#         if left > tr or right < tl:
#             return
#         if tl <= left <= right <= tr:
#             self.tree[idx] += value
#             self.lazy[idx] += value
#             return
#         l, r = idx << 1, (idx << 1) + 1
#         mid = (l + r) >> 1
#
#         self.push_down(idx)
#         self.update(l, left, mid, tl, tr, value)
#         self.update(r, mid + 1, right, tl, tr, value)
#         self.tree[idx] = self.tree[l] + self.tree[r]
#
#     def query(self, idx, left, right, tl, tr):
#         if left > tr or right < tl:
#             return float("-inf")
#         if tl <= left <= right <= tr:
#             return self.tree[idx]
#         l, r = idx << 1, (idx << 1) + 1
#         mid = (l + r) >> 1
#         self.push_down(idx)
#         return self.query(l, left, mid, tl, tr) + self.query(r, mid + 1, right, tl, tr)
#
#
# if __name__ == "__main__":
#     tc = int(input())
#     for t in range(1, tc + 1):
#         n, q = list(map(int, input().split()))
#         nums = list(map(int, input().split()))
#         seg_tree = SegmentTree(nums)
#         print("Case %s" % t)
#         for _ in range(q):
#             qr = list(map(int, input().split()))
#             if qr[0] == 1:
#                 idx = qr[1]
#                 print(seg_tree.nums[idx])
#                 seg_tree.update(idx, 0, n - 1, 0, n - 1, -seg_tree.nums[idx])
#                 seg_tree.nums[idx] = 0
#             if qr[0] == 2:
#                 idx = qr[1]
#                 value = qr[2]
#                 seg_tree.update(idx, 0, n - 1, 0, n - 1, value)
#                 seg_tree.nums[idx] += value
#             if qr[0] == 3:
#                 fr, to = qr[1], qr[2]
#                 print(seg_tree.query(0, fr, to, 0, n - 1))


import math


def main():
    t = int(input())

    for case_number in range(1, t + 1):
        print("Case {0}:".format(case_number))

        n, q = map(int, input().split())
        a = list(map(int, input().split()))

        h = int(math.ceil(math.log2(n)))
        tree_size = int(2 * math.pow(2, h) - 1)
        seg_tree = [0 for i in range(tree_size)]

        build_tree(a, seg_tree, 0, 0, n - 1)

        for _ in range(q):
            line = input().split()

            if line[0] == '1':
                i = int(line[1])
                print(a[i])
                update_tree(seg_tree, 0, 0, n - 1, i, -a[i])
                a[i] = 0
            elif line[0] == '2':
                i = int(line[1])
                v = int(line[2])
                update_tree(seg_tree, 0, 0, n - 1, i, v)
                a[i] += v
            else:
                i = int(line[1])
                j = int(line[2])
                print(sum_range(seg_tree, 0, 0, n - 1, i, j))


def sum_range(seg_tree, index, left, right, range_from, range_to):
    if left > range_to or right < range_from:
        return 0

    if range_from <= left and right <= range_to:
        return seg_tree[index]

    mid = (left + right) // 2

    return sum_range(seg_tree, 2 * index + 1, left, mid, range_from, range_to) \
         + sum_range(seg_tree, 2 * index + 2, mid + 1, right, range_from, range_to)


def update_tree(seg_tree, index, left, right, pos, val):
    if pos < left or pos > right:
        return

    if left == right:
        if left == pos:
            seg_tree[index] += val
        return

    mid = (left + right) // 2

    update_tree(seg_tree, 2 * index + 1, left, mid, pos, val)
    update_tree(seg_tree, 2 * index + 2, mid + 1, right, pos, val)

    seg_tree[index] = seg_tree[2 * index + 1] + seg_tree[2 * index + 2]


def build_tree(a, seg_tree, index, left, right):
    if left == right:
        seg_tree[index] = a[left]
        return

    mid = (left + right) // 2

    build_tree(a, seg_tree, 2 * index + 1, left, mid)
    build_tree(a, seg_tree, 2 * index + 2, mid + 1, right)

    seg_tree[index] = seg_tree[2 * index + 1] + seg_tree[2 * index + 2]


if __name__ == '__main__':
    main()