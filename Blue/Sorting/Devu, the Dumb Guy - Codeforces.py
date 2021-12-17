if __name__ == "__main__":
    inputs = list(map(int, input().split()))
    subjects = list(map(int, input().split()))
    subjects.sort()
    x = inputs[1]
    ans = 0
    for val in subjects:
        ans += val * x
        if x > 1:
            x -= 1
    print(ans)
