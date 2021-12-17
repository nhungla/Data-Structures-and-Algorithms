class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)

        self.build_tree(0, 0, len(self.tree) - 1)

    def build_tree(self, idx, left, right):
        if left == right:
            self.tree[idx] = self.nums[left]
            return
        mid = (left + right) >> 1
        self.build_tree(2 * idx, left, mid)
        self.build_tree(2 * idx + 1, mid + 1, right)
        self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def push_down(self, idx):
        if self.lazy[idx] == 0:
            return
        left, right = idx << 1, (idx << 1) + 1
        self.lazy[left] = self.lazy[right] = self.lazy[idx]
        self.tree[left] = self.tree[right] = self.lazy[idx]
        self.lazy[idx] = 0

    def update(self, idx, left, right, tl, tr, value):
        if left > tr or right < tl:
            return
        if tl <= left <= right <= tr:
            self.tree[idx] += value
            self.lazy[idx] += value
            return
        l, r = idx << 1, (idx << 1) + 1
        mid = (l + r) >> 1

        self.push_down(idx)
        self.update(l, left, mid, tl, tr, value)
        self.update(r, mid + 1, right, tl, tr, value)
        self.tree[idx] = self.tree[l] + self.tree[r]

    def query(self, idx, left, right, tl, tr):
        if left > tr or right < tl:
            return float("-inf")
        if tl <= left <= right <= tr:
            return self.tree[idx]
        l, r = idx << 1, (idx << 1) + 1
        mid = (l + r) >> 1
        self.push_down(idx)
        return self.query(l, left, mid, tl, tr) + self.query(r, mid + 1, right, tl, tr)