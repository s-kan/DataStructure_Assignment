import sys
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    a[1] = a[0]+a[1]
    arr.append(a)

m = arr[0][0]
M = arr[0][1]
for i in arr:
    if i[0] < m:
        m = i[0]
    if i[1] > M:
        M = i[1]

r = 0
for i in range(m, M+1):
    temp = 0
    for j in arr:
        if j[0]<=i<j[1]:
            temp += 1
    if temp>=r:
        r = temp
print(r)