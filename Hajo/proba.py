import itertools as it

sor=[1,2,3,4]
perm= list(it.permutations(sor))
print(perm)
perm.remove(perm[1])
perm.remove(perm[0])
print(perm)