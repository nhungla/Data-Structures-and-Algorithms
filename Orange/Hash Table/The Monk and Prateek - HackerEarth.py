# import collections
#
#
# def hash_function(n):
#     ss = 0
#     tmp = n
#     while n:
#         ss += n % 10
#         n = n // 10
#     return tmp ^ ss
#
#
# if __name__ == "__main__":
#     n = int(input())
#     nums = list(map(int, input().split()))
#     map_nums = collections.defaultdict(list)
#     for val in nums:
#         key = hash_function(val)
#         map_nums[key].append(val)
#     if len(map_nums) == n:
#         print("%s %s" % (max(map_nums.keys()), 0))
#         exit()
#     ans, max_count, max_val = 0, 0, 0
#     for k, v in map_nums.items():
#         max_val = max(max_val, k)
#         if len(v) > max_count:
#             max_count = len(v)
#             ans = k
#         elif len(v) == max_count:
#             ans = min(ans, k)
#     print("%s %s" % (ans, max_count - 1))
#

import math

def sumOfDigit(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

def hashFunc(n):
    return n^sumOfDigit(n)

nCollision = 0
maxHashValue = -1
minHashValueCollision = 10 ** 9
maxFrequency = -1
mp = dict()

n = int(input())
a = list(map(int, input().split()))
for num in a:
    hash_value = hashFunc(num)
    maxHashValue = max(maxHashValue, hash_value)
    if hash_value in mp:
        mp[hash_value] += 1
    else:
        mp[hash_value] = 1

for item in mp:
    nCollision += mp[item] - 1
    maxFrequency = max(maxFrequency, mp[item])

if len(mp) == n:
    print(maxHashValue, end = " ")
else:
    for item in mp:
        if mp[item] == maxFrequency:
            minHashValueCollision = min(item, minHashValueCollision)
    print(minHashValueCollision, end = " ")
print(nCollision)
