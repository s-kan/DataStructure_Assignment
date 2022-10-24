import sys

m, n = map(int, sys.stdin.readline().split())
a = []
arr = []
while(1):
    A = list(sys.stdin.readline().rstrip())
    if A[0] == '-':
        break
    a += map(int, A)

cnt = a.count(1)


for i in range(0, m*n, m):
    arr.append(a[i:i+m])

b_state = []

for i in range(1, n-1):
    state = 0
    b = l = 0

    if arr[i].count(1) == 0:
        continue

    for j in range(1, m-1):
        # 1을 만났을 경우
        if arr[i][j] == 1:
            if state == 0:
                # 닫는 뚜껑인지 확인하는 for문
                for k in b_state:
                    if j == k or j == k-1:
                        b_state.remove(k)
                        state = -1
                if state == -1:
                    continue
                # 닫는 1 일 때
                elif arr[i][j - 1] == 2:
                    state = 0
                # 여는 1 일 때
                elif arr[i][j - 1] == 0:
                    state = 1
            else:
                continue


        elif arr[i][j] == 0:
            if state == 1:
                l += 1
                if arr[i+1][j] == 1:
                    b += 1

                if arr[i-1][j] == 2 or arr[i-1][j] == 1:
                    arr[i][j] = 2
                    cnt += 1
                else:
                    state = 0
                    continue

                if arr[i][j+1] == 1:
                    if l == b:
                        b_state.append(j-l+1)
                        l=b=0
                    state = 0
            elif state == -1:
                state = 0
            elif state == 0 and arr[i-1][j+1] == 2 and arr[i][j-1] == 1:
                state = 1
                arr[i][j] = 2
                cnt += 1

print(cnt)

