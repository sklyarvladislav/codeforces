import sys
from math import ceil
n, m, a = list(map(int, sys.stdin.readline().split()))
print(ceil(n/a)*ceil(m/a))