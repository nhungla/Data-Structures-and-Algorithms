# có 2^m trạng thái khi xếp domino vào
def solve(no_space, no_piece, pieces, start, end):
    dp = [[False] * 7 for _ in range(1 << no_piece)]
    dp[0][start[1]] = True
    for mask in range(1 << no_piece):
        for last in range(7):
            # giá trị thứ 2 của domino cuối được đặt vào
            if not dp[mask][last]:
                continue
            for i, (x, y) in enumerate(pieces):
                if last != x and last != y:
                    continue
                if not ((mask >> i) & 1):
                    if x == last:
                        dp[mask ^ (1 << i)][y] = True
                    else:
                        dp[mask ^ (1 << i)][x] = True
    for mask in range(1 << no_piece):
        if bin(mask).count("1") == no_space and dp[mask][end[0]]:
            return True
    return False


if __name__ == "__main__":
    while True:
        no_space = int(input())
        if not no_space:
            break
        no_piece = int(input())
        start = list(map(int, input().split()))
        end = list(map(int, input().split()))
        pieces = []
        for _ in range(no_piece):
            pieces.append(list(map(int, input().split())))

        ans = solve(no_space, no_piece, pieces, start, end)
        print("YES" if ans else "NO")
