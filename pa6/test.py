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

# 출력할 총 넓이인 cnt를 먼저 경계선 넓이로 초기화
cnt = a.count(1)

# 일차원 배열읠 이차원 배열로 변환

for i in range(0, m*n, m):
    arr.append(a[i:i+m])
for i in range(m):
    for j in range(n):
       print(arr[i][j], end=' ')
    print()
print('---------------------')

# state는 열었을 때 왼쪽과 위가 1인 경우 0을 1로 바꾼다
b_state = []
# c_state 는 경계선 내부에 있는 1이 닫는 1이 아니라는 것을 판단 하기 위한
for i in range(1, n-1):
    state = 0
    b = l = 0
    # 행에 1의 개수가 0개라면 그냥 넘어감
    if arr[i].count(1) == 0:
        continue
    # 행에 1이 있다면 그 행을 조사
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

        # 0을 만났을 경우
        elif arr[i][j] == 0:
            if state == 1:
                l += 1
                if arr[i+1][j] == 1:
                    b += 1
                # 경계선 안의 0인지 밖의 0인지 판단
                if arr[i-1][j] == 2 or arr[i-1][j] == 1:
                    arr[i][j] = 2
                    cnt += 1
                else:
                    state = 0
                    continue
                # 닫을려고 할 때 밑의 1들이 닫는 뚜껑인지 확인하기 위한 b_state에 값 추가
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

for i in range(m):
   for j in range(n):
       print(arr[i][j], end=' ')
   print()
print(cnt)

