import collections


def getOpenings(matrix, rowNum, colNum):
    openings = []
    cloned = [row[:] for row in matrix]
    for i in range(colNum):
        if cloned[0][i] == '.':
            cloned[0][i] = '#'
            openings.append([0, i])
        if cloned[rowNum-1][i] == '.':
            cloned[rowNum-1][i] = '#'
            openings.append([rowNum-1, i])

    for i in range(rowNum):
        if cloned[i][0] == '.':
            cloned[i][0] = '#'
            openings.append([i, 0])
        if cloned[i][colNum-1] == '.':
            cloned[i][colNum-1] = '#'
            openings.append([i, colNum-1])

    return openings


def isValid(matrix, start, end, rowNum, colNum):
    queue = collections.deque([start])
    seen = {(start[0], start[1])}
    while queue:
        x, y = queue.popleft()
        if x == end[0] and y == end[1]:
            return True
        cands = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        for a, b in cands:
            if 0 <= a < rowNum and 0 <= b < colNum and matrix[a][b] == '.' and (a, b) not in seen:
                seen.add((a, b))
                queue.append([a, b])
    return False


def main():
    testNum = int(input())
    for _ in range(testNum):
        rowNum, colNum = list(map(int, input().split()))
        matrix = []
        for _ in range(rowNum):
            matrix.append(list(input()))
        openings = getOpenings(matrix, rowNum, colNum)
        if len(openings) == 2:
            if isValid(matrix, openings[0], openings[1], rowNum, colNum):
                print('valid')
            else:
                print('invalid')
        else:
            print('invalid')


if __name__ == "__main__":
    main()