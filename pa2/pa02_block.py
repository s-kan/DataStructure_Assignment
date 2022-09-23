import sys

# hl, hr 입력 및 배열 저장
hl = list(map(int, sys.stdin.readline().split()))
hr = list(map(int, sys.stdin.readline().split()))

hl.remove(-9)
hr.remove(-9)

# 보도블럭의 위치를 나타내기 위한 이차원 배열 선언
M = len(hl)

if hr[hl.index(max(hl))] == -1:
    N=max(hl)
else:
    N=max(hl)+1

A = [[0]*N for i in range(M)]

vt = [0]*N
vb = [0]*N

# 2차원 배열로 보도블럭의 위치 표시
for i in range(M):
    for j in range(hl[i]):
        A[i][j] = A[i][j]+1
    for k in range(N-1, N-1-hr[i], -1):
        A[i][k] = A[i][k]+1

# vt 결정
for i in range(N):
    for j in range(M):
        if A[j][i] == 1:
            vt[i]=vt[i]+1
        else:
            break

# vb 결정
for i in range(N):
    if vt[i]==M:
        vb[i]=-1
    else:
        for j in range(M-1, -1, -1):
            if A[j][i]==1:
                vb[i]=vb[i]+1
            else:
                break

vt.append(-9)
vb.append(-9)

for i in vt:
    print(i, end=' ')
print()
for i in vb:
    print(i, end=' ')