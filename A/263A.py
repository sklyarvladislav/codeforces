import sys
column = 0
row = 0
flag = False
for i in range(5):
    row += 1
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        if data[j] == 1:
            column = j
            flag = True
            break
    if flag == True:
        break
print(abs(3-(column+1))+abs(3-row))
