import sys

# 입력부
m, n = map(int, sys.stdin.readline().split())
a = []
arr = []
while(1):
    A = list(sys.stdin.readline().rstrip())
    if A[0] == '-':
        break
    a += map(int, A)

# 일차원 배열읠 이차원 배열로 변환
for i in range(0, m*n, m):
    arr.append(a[i:i+m])

cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            arr[i][j] = 2
            cnt += 1
        elif arr[i][j] == 2:
            continue
        else:
            break

for i in range(n):
    for j in range(m-1, -1, -1):
        if arr[i][j] == 0:
            arr[i][j] = 2
            cnt += 1
        elif arr[i][j] == 2:
            continue
        else:
            break

for j in range(m):
    for i in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 2
            cnt += 1
        elif arr[i][j] == 2:
            continue
        else:
            break

for j in range(m):
    for i in range(n-1, -1, -1):
        if arr[i][j] == 0:
            arr[i][j] = 2
            cnt += 1
        elif arr[i][j] == 2:
            continue
        else:
            break
for i in range(m):
   for j in range(n):
       print(arr[i][j], end=' ')
   print()
print(m*n-cnt)