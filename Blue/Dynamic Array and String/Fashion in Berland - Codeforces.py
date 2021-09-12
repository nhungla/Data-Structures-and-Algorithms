def fashion_in_berland(arr):
    n = len(arr)
    if n < 2:
        return True if arr[0] == '1' else False

    count = 0
    for i, val in enumerate(arr):
        if val == '0':
            count += 1
        if count > 1:
            return False
    return True if count == 1 else False


if __name__ == "__main__":
    n = input()
    arr = input().split()
    if fashion_in_berland(arr):
        print("YES")
    else:
        print("NO")
