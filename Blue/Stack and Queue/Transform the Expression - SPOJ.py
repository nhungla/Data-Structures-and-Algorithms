import collections


def transform(exp):
    chars = collections.deque()
    operators = []
    ans = ''
    for e in exp:
        if e in ['+', '-', '*', '/', '^', '(']:
            if operators and e > operators[-1]:
                while e and operators[-1] != '(':
                    chars.append(operators.pop())
            operators.append(e)
        if 'a' <= e <= 'z':
            chars.append(e)
        if e == ')':
            while operators[-1] != '(':
                chars.append(operators.pop())
            operators.pop()
    while operators:
        chars.append(operators.pop())
    return list(chars)


if __name__ == "__main__":
    n = int(input())
    expressions = []
    for i in range(n):
        expressions.append(list(input()))
    stack = []

    for e in expressions:
        val = transform(e)
        print(''.join(val))