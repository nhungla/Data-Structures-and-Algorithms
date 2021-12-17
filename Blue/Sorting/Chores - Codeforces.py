if __name__ == "__main__":
    inputs = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    p, v = inputs[1], inputs[2]
    arr.sort()
    ans = arr[v] - arr[v - 1]
    print(ans)
