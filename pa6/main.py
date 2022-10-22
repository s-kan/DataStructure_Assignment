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
cnt = a.count(1)
# 일차원 배열읠 이차원 배열로 변환
for i in range(0, m*n, m):
    arr.append(a[i:i+m])
for i in range(m):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()

# 2차원 배열에 따라서 조사 시작
# cnt는 출력할 섬의 총 넒이, state는 경계선인 1을 만났을 때 다음이 0인 경우
# 포함 해야 하는 것인지 아닌지를 확일 할 수 있는 정보
# r, l는 cnt에 넣기 전, 양 쪽의 column 위치 차를 이용 해서 센다
state = 0
l, r  = 0, 0

for i in range(n):
    # 행에 1의 개수가 0개라면 그냥 넘어감
    if arr[i].count(1) == 0:
        continue
    # 행에 1이 있다면 그 행을 조사
    for j in range(m):
        # 1인 경우
        if arr[i][j] == 1:
            # 처음 만난 1인 경우 l을 갱신
            if state == 0:
                l = j
                state = 1
            # 열리고 나서 만난 1이고 다음이 0인 경우 닫을 것인지 계속 열 것인지 판단을 한다.
            elif state == 1:
                continue

        # 0이고 state가 1인 경우
        elif arr[i][j] == 0 and state == 1:
            # 0이 경계선 안에 있는 경우
            if arr[i-1][j] == 1:
                print('hi')
                arr[i][j] = 1
                cnt += 1
            # 0이 경계선 밖에 있는 경우 state 갱신으로 닫아주고, r 갱신
            else:
                state = 0
                r = j-1
print()
for i in range(m):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
print(cnt)
