import collections
if __name__ == "__main__":
  tc = int(input())
  input()
  for _ in range(tc):
    trees = collections.Counter()
    total = 0
    read = True
    while read:
      try:
        tree = input()
        if not tree:
          break
        trees[tree] += 1
        total += 1
      except Exception as ex:
        read = False
        pass
    ans = []
    #print(trees, len(trees))
    if total == 0:
      break
    names = [val for val in trees.keys()]
    names.sort()
    for na in names:
      print("%s %s" %(na, format(trees[na]/total * 100.0, ".4f")))
    print()