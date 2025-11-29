import sys

n = int(sys.stdin.readline())
x = 0
for i in range(n):
    a = sys.stdin.readline()
    if '-' in a: x -= 1
    if '+' in a: x += 1

print(x)