if __name__ == "__main__":
  tc = int(input())
  for _ in range(tc):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    set_val = set(arr)
    if len(set_val) == x:
      print("Good")
    elif len(set_val) < x:
      print("Bad")
    else:
      print("Average")