class Node:
  def __init__(self, rank=-1):
    self.child = {}
    self.rank = rank
  def __repr__(self):
    return "%s - %s" % (self.child, self.rank)
class Trie:
  def __init__(self):
    self.root = Node()
  def __repr__(self):
    return "%s" % (self.root)
  def add_word(self, word, rank):
    r = self.root
    for w in word:
      if w not in r.child:
        r.child[w] = Node(rank)
      r = r.child[w]
      r.rank = rank

  def query(self, word):
    r = self.root
    cur_rank = -1
    for w in word:
      if w not in r.child:
        return -1
      cur_rank = r.child[w].rank
      r = r.child[w]
    return cur_rank
if __name__ == "__main__":
  n, q = list(map(int, input().split()))
  trie = Trie()
  tmp = []
  for _ in range(n):
    word, rank = input().split()
    #trie.add_word(word, int(rank))
    tmp.append((word, int(rank)))
  tmp.sort(key=lambda x: x[1])
  for w, r in tmp:
    trie.add_word(w, r)
  for _ in range(q):
    ans = trie.query(input())
    print(ans)