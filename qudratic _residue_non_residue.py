# script calculates quadratic residue and non residue modulo of an odd prime

p = 13

k = p // 2

residue = []
non_residue = []
for i in range(1, k + 1):
    residue.append(i ** 2 % p)
for i in range(1, p + 1):
    if i not in residue:
        non_residue.append(i)

print(residue)
print(non_residue)
