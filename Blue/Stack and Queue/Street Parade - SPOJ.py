if __name__ == "__main__":
    testcase = int(input())
    while testcase != 0:
        count = 1
        trucks = list(map(int, input().split()))
        stack = []
        for val in trucks:
            if val == count:
                count += 1
            else:
                while stack and stack[-1] == count:
                    stack.pop()
                    count += 1
                stack.append(val)

        while stack and stack[-1] == count:
            stack.pop()
            count += 1
        print('yes') if len(stack) == 0 else print('no')
        testcase = int(input())
        