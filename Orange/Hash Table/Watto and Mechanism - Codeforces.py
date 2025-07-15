def init():
    f1[0] = f2[0] = 1
    for i in range(1, L):
        f1[i] = (f1[i - 1] * a) % table_size_1
        f2[i] = (f2[i - 1] * a) % table_size_2


def polyHash(keys, mod):
    hashValue = 0
    for i in range(len(keys)):
        hashValue = (hashValue * a + ord(keys[i])) % mod

    return hashValue


def check(query):
    h1 = polyHash(query, table_size_1)
    h2 = polyHash(query, table_size_2)

    leng = len(query)
    for i in range(leng):
        for c in range(3):
            c_char = chr(ord('a') + c)
            if c_char == query[i]:
                continue
            new_hashValue_1 = ((((ord(c_char) - ord(query[i])) * f1[
                leng - i - 1]) % table_size_1 + table_size_1) + h1) % table_size_1
            new_hashValue_2 = ((((ord(c_char) - ord(query[i])) * f2[
                leng - i - 1]) % table_size_2 + table_size_2) + h2) % table_size_2
            if (new_hashValue_1, new_hashValue_2) in dic:
                return True
    return False


L = 1000001
table_size_1 = int(1e9) + 7
table_size_2 = int(1e9) + 9

a = 257
f1 = [0] * L
f2 = [0] * L

init()

n, m = map(int, input().split())
dic = set()
for i in range(n):
    keys = input()
    dic.add((polyHash(keys, table_size_1), polyHash(keys, table_size_2)))

buf = []

for i in range(m):
    t = input()
    buf.append('YES' if check(t) else 'NO')
print('\n'.join(buf))