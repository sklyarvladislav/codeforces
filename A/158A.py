import sys
n, k = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
res_k = a[k-1]
if res_k == 0:
    res = 0
    i = 0
    while a[i] > 0:
        res += 1
        i += 1
    print(res)
else:
    res = k
    i = k
    while i < n and a[i] == res_k:
        res += 1
        i += 1 
    print(res)