IS_LEAF = "is_leaf"
class Trie:
  def __init__(self):
    self.root = {}
  def add_word(self, word):
    r = self.root
    for w in word:
      r = r.setdefault(w, {})
      if r.get(IS_LEAF):
        return True
    r[IS_LEAF] = True
    for ch in range(ord('a'), ord('k')):
      ch = chr(ch)
      if ch in r:
        return True
    return False
if __name__ == "__main__":
  n = int(input())
  tree = Trie()
  ans = None
  for _ in range(n):
    word = input()
    if tree.add_word(word):
      ans = word
      break
  print("GOOD SET") if ans is None else print("BAD SET\n%s" % ans)