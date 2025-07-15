from sys import stdin, stdout
from queue import Queue

def main():
    global io
    io = Stdio()

    n = io.next_int()
    names = []

    for i in range(n):
        names.append(io.next())

    lexicographical = set_up_lexicographical(names)

    if lexicographical == None:
        io.println("Impossible")
        return

    result = topo_sort(lexicographical)

    if result == None:
        io.println("Impossible")
        return

    io.println(result)


def set_up_lexicographical(names):
    lexicographical = [[] for u in range(26)]
    relation = [[False for v in range(26)] for u in range(26)]

    for i in range(len(names) - 1):
        flag = False
        min_size = min(len(names[i]), len(names[i + 1]))

        for j in range(min_size):
            if names[i][j] != names[i + 1][j]:
                relation[ord(names[i][j]) - 97][ord(names[i + 1][j]) - 97] = True
                flag = True
                break

        if not flag and len(names[i]) > len(names[i + 1]):
            return None

    for i in range(26):
        for j in range(26):
            if relation[i][j]:
                lexicographical[i].append(j)

    return lexicographical


def topo_sort(lexicographical):
    in_deg = [0 for u in range(26)]
    result = []
    zero_in_deg_queue = Queue()

    for u in range(26):
        for v in lexicographical[u]:
            in_deg[v] += 1

    for u in range(26):
        if in_deg[u] == 0:
            zero_in_deg_queue.put(u)

    while not zero_in_deg_queue.empty():
        u = zero_in_deg_queue.get()
        result.append(chr(u + 97))

        for v in lexicographical[u]:
            in_deg[v] -= 1

            if in_deg[v] == 0:
                zero_in_deg_queue.put(v)

    for u in range(26):
        if in_deg[u] != 0:
            return None

    return ''.join(str(c) for c in result)


class Stdio:
    index = 0
    tokens = []
    line = None

    def next_line(self):
        tokens = []
        return stdin.readline()

    def next(self):
        while (self.index >= len(self.tokens)):
            self.tokens = self.next_line().strip().split()
            if len(self.tokens) == 0:
                return None
            self.index = 0
        token = self.tokens[self.index]
        self.index += 1
        return token

    def next_int(self):
        return int(self.next())

    def next_float(self):
        return float(self.next())

    def next_char(self):
        return chr(self.next())

    def print(self, *objects):
        for obj in objects:
            stdout.write(str(obj))

    def println(self, *objects):
        for obj in objects:
            stdout.write(str(obj))
        stdout.write('\n')


if __name__ == "__main__":
    main()