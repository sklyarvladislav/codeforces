import sys
n, k = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
res_k = a[k-1]
res = 0
if res_k == 0:
    print(res)
else:
    res = len(a[:k])
    i = k
    while a[i] == res_k and i < n:
        res += 1
        i += 1 
    print(res)