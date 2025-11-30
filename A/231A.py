import sys

n = int(sys.stdin.readline())
k = 0 
for i in range(n):
    if sum(list(map(int, sys.stdin.readline().split()))) >= 2:
        k += 1
print(k)