if __name__ == "__main__":
  n = int(input())
  nums = list(map(int, input().split()))
  nums.sort()
  ans = 0
  for idx, val in enumerate(nums):
    ans += abs(idx + 1 - val)
  print(ans)