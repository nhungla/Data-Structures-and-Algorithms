atom = []
mass = lambda c: 1 if c == 'H' else 12 if c == 'C' else 16

for c in input().strip():
    if c.isalpha():
        atom.append(mass(c))
    elif c.isnumeric():
        mol = atom[-1] * int(c)
        atom.pop()
        atom.append(mol)
    elif c == '(':
        atom.append(-1)
    elif c == ')':
        w = 0
        while atom[-1] != -1:
            w += atom[-1]
            atom.pop()
        atom.pop()
        atom.append(w)

print(sum(atom))