from itertools import permutations
import sys
n = int(sys.argv[1])
global_ans = 0
perms = permutations(range(n))
a = next(perms, None)
while a != None:
    ans = 0
    for i in range(n):
        index = 0
        for r in range(-i, n-i):
            if r != 0 and (a[index] == a[i] + r or a[index] == a[i] - r):
                break
            index += 1
            if index == n:
                ans += 1
    a = next(perms, None)
    if ans == n:
        global_ans += 1
        print(a)
print(global_ans)