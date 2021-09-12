if __name__ == "__main__":
    n1, n2 = list(map(int, input().split()))
    k, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print('YES') if A[k - 1] < B[n2 - m] else print('NO')