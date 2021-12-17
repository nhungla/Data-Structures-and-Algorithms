import collections
if __name__ == "__main__":
  n = int(input())
  while n != 0:
    arr = [val for val in range(1, n + 1)]
    ans = []
    stack = collections.deque(arr)
    add = True
    while len(stack) > 1:
      if add:
        ans.append(stack.popleft())
        add = False
      else:
        p = stack.popleft()
        stack.append(p)
        add = True
    if ans:
      string = 'Discarded cards: ' + ', '.join(map(str, ans))
    else:
      string = 'Discarded cards:'
    print(string)
    print('Remaining ca