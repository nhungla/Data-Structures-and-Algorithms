if __name__ == "__main__":
  n = int(input())
  arr = []
  for i in range(n):
    id, cur, p, l , c, s = list(map(int, input().split()))
    new_score = p * 50 + l * 5 + c * 10 + s * 20
    arr.append([id, cur, new_score])
  arr.sort(key=lambda x: (-abs(x[2] - x[1]), -x[0]))
  for i in range(5):
    print(arr[i][0], arr[i][2])