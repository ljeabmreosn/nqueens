from itertools import permutations
import sys
def fun(a, n):
    for i in range(n):
        index = 0
        for r in range(-i, n-i):
            if r != 0 and (a[index] == a[i] + r or a[index] == a[i] - r):
                return 0
            index+=1
    return 1
n = int(sys.argv[1])
ans = 0
perms = permutations(range(n))
a = next(perms, None)
while a != None:
    ans += fun(a, n)
    a = next(perms, None)
print(ans)
