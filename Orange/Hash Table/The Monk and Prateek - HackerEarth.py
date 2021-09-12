import collections


def hash_function(n):
    ss = 0
    tmp = n
    while n:
        ss += n % 10
        n = n // 10
    return tmp ^ ss


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    map_nums = collections.defaultdict(list)
    for val in nums:
        key = hash_function(val)
        map_nums[key].append(val)
    if len(map_nums) == n:
        print("%s %s" % (max(map_nums.keys()), 0))
        exit()
    ans, max_count, max_val = 0, 0, 0
    for k, v in map_nums.items():
        max_val = max(max_val, k)
        if len(v) > max_count:
            max_count = len(v)
            ans = k
        elif len(v) == max_count:
            ans = min(ans, k)
    print("%s %s" % (ans, max_count - 1))
