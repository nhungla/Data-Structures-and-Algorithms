from itertools import permutations


class Block:
    def __init__(self, i):
        self.dimension = i

    def __lt__(self, other):
        for i in range(3):
            if self.dimension[i] > other.dimension[i]:
                return True
            if self.dimension[i] < other.dimension[i]:
                return False
        return True

    def __str__(self):
        return str(self.dimension[0]) + " " + str(self.dimension[1]) + \
               " " + str(self.dimension[2])

    def can_stack(self, other):
        if self.dimension[0] < other.dimension[0] and self.dimension[1] < other.dimension[1]:
            return True
        return False


def build_blocks(blocks, arr):
    arr.sort()
    b = list(permutations(arr))
    for i in b:
        blocks.append(Block(i))


def lis(blocks):
    n = len(blocks)
    heights = [block.dimension[2] for block in blocks]
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if blocks[i].can_stack(blocks[j]):
                heights[i] = max(heights[i], heights[j] + blocks[i].dimension[2])
    return max(heights)


if __name__ == "__main__":
    testcase = 1
    while True:
        n = int(input())
        if n == 0:
            break
        blocks = []
        for _ in range(n):
            arr = list(map(int, input().split()))
            build_blocks(blocks, arr)
        blocks.sort()
        ans = lis(blocks)
        print("Case %s: maximum height = %s" % (testcase, ans))
        testcase += 1
