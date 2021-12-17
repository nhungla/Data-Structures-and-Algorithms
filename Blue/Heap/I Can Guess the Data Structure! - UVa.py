import collections
import heapq
if __name__ == "__main__":
  while True:
    try:
      n = int(input())
    except EOFError:
      break
    st, q, pq = [], collections.deque(), []
    is_st = is_q = is_pq = True
    for i in range(n):
      k, v = list(map(int, input().split()))
      if k == 1:
        st.append(v)
        q.append(v)
        heapq.heappush(pq, -v)
      else:
        if v != st.pop():
          is_st = False
        if v != q.popleft():
          is_q = False
        if -v != heapq.heappop(pq):
          is_pq = False
    if not is_st and not is_q and not is_pq:
      print("impossible")
    elif is_st + is_q + is_pq > 1:
      print("not sure")
    elif is_st:
      print("stack")
    elif is_q:
      print("queue")
    elif is_pq:
      print("priority queue")