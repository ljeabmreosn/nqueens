def cond(p, i):
    for r in range(i):
        if abs(p[i]-p[r]) == abs(i-r):
            return False
    return True
def level(p, a, i, n):
    if i >= n:
       print(p)
    else:
        for x in range(len(a)):
            p[i] = a[x]
            if cond(p, i):
                level(p, a[:x]+a[x+1:], i+1, n)
def perms(n):
    level([0]*n, list(range(1, n+1)), 0, n)
while True:
    perms(int(input()))
