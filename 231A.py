n = int(input())
k = 0 
for i in range(n):
    if sum(list(map(int, input().split()))) >= 2:
        k += 1
print(k)