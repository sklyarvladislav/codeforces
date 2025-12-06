import sys

first = sys.stdin.readline().strip().lower()
second = sys.stdin.readline().strip().lower()

if first == second:
    print(0)
elif first < second:
    print(-1)
else:
    print(1)