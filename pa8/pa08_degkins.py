n = int(input())
arr = []
# 우선 입력 받는 [부모 노드, 자식 노드]의 정보를 2차원 배열에 저장 한다.
for i in range(n):
    arr.append(input().split())
# 촌수를 구할 노드를 배열에 입력 받는다.
src = []
for i in range(2):
    src.append(input())

# 촌수를 구할 두 노드(src)의 상위 노드들을 각각 p_arr0, p_arr1 에 다 넣는다.
p_arr0 = []
p_arr1 = []
src_ia = src_ib = 0
for i in range(len(arr)):
    if src[0] == arr[i][1]:
        src_ia = i
for i in range(len(arr)):
    if src[1] == arr[i][1]:
        src_ib = i

s = src[0]
for i in range(src_ia, -1, -1):
    if arr[i][1] == s:
        p_arr0.append(arr[i][0])
        s = arr[i][0]
s = src[1]
for i in range(src_ib, -1, -1):
    if arr[i][1] == s:
        p_arr1.append(arr[i][0])
        s = arr[i][0]
p = ''
for i in range(len(p_arr0)-1, -1, -1):
    for j in range(len(p_arr1)-1, -1, -1):
        if p_arr0[i] == p_arr1[j]:
            p = p_arr0[i]

# p_arr0 와 p_arr1 에 있는 각각의 부모 노드 배열의 끝에서
# src 두 노드의 공통 부모까지의 거리 합이 구하는 값이다.
rlt1 = 0
rlt2 = 0

for i in p_arr0:
    if p == i:
        rlt1 += 1
        break
    else:
        rlt1 += 1

for i in p_arr1:
    if p == i:
        rlt2 += 1
        break
    else:
        rlt2 += 1
if src[0] == src[1]:
    rlt1 = rlt2 = 0
print(rlt1+rlt2)
