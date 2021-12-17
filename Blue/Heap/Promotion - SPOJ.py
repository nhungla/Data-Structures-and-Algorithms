import heapq

if __name__ == "__main__":
    n = int(input())
    max_receipt = []
    min_receipt = []
    num_bill = 0
    ans = 0
    used = [False] * (10 ** 6 + 1)
    for i in range(n):
        arr = list(map(int, input().split()))

        for v in arr[1:]:
            num_bill += 1
            heapq.heappush(max_receipt, (-v, num_bill))
            heapq.heappush(min_receipt, (v, num_bill))
        while used[min_receipt[0][1]]:
            heapq.heappop(min_receipt)
        while used[max_receipt[0][1]]:
            heapq.heappop(max_receipt)

        used[min_receipt[0][1]] = used[max_receipt[0][1]] = True
        ans += -heapq.heappop(max_receipt)[0] - heapq.heappop(min_receipt)[0]
    print(ans)