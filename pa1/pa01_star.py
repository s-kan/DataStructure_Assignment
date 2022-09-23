import sys, heapq

# 선언, 입력
n = int(sys.stdin.readline())
arr = []
height = [0] * n
q = []
count = 0


end = [0] * n

check = set()

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    # arr -> (건물 정보, index, 1:시작점,-1:끝점)
    arr.append((a, i, 1))
    arr.append((a+c, i, -1))
    height[i] = b
    end[i] = a+c

arr.sort(key=lambda x: (x[0], -x[2], -height[x[1]]))
# ans에 스카이라인의 정보를 따로 넣음
# -> 스카이 라인의 높이가 바뀔 때의 x좌표와 그 때의 높이 정보
now = 0
ans = []
for i in range(len(arr)):
    point, idx, dir = arr[i]

    if dir == 1:
        if now < height[idx]:
            now = height[idx]
            ans.append((point, now))
            count = count+1
        heapq.heappush(q, (-height[idx], end[idx]))

    else:
        check.add(point)
        while q:
            if q[0][1] not in check:
                break
            heapq.heappop(q)
        if not q:
            if now:
                now = 0
                ans.append((point, now))
                count = count+1
        else:
            if -q[0][0] != now:
                now = -q[0][0]
                ans.append((point, now))
                count = count+1
                
# 확일 할 별의 좌표 입력
star = []
k = int(sys.stdin.readline())
for i in range(k):
    star.append((list(map(int, sys.stdin.readline().split()))))
    
# 별의 위치 확인, 출력
#->배열 ans의 스카이라인 정보와 별의 좌표를 비교연산을 해서 별의 위치 확인
for i in star:
    # 별이 스카이라인 시작 부분 전, 끝 부분 후에 있을 때
    if (i[0] < ans[0][0]) or (i[0] > ans[-1][0]):
        if i[1] > 0:
            print('over')
        else:
            print('on')
    # 별이 스카이라인 시작 부분에 걸칠 때
    elif i[0] == ans[0][0]:
        if i[1] <= ans[0][1]:
            print('on')
        else:
            print('over')
    # 별이 스카이라인 끝 부분에 걸칠 때
    elif i[0] == ans[-1][0]:
        if i[1] <= ans[-2][1]:
            print('on')
        else:
            print('over')
    # 별이 스카이라인의 시작과 끝 사이에 존재할 때
    else:
        for k in range(count):
            if ans[k][0] < i[0] < ans[k+1][0]:
                if ans[k][1] < i[1]:
                    print('over')
                elif ans[k][1] > i[1]:
                    print('under')
                else:
                    print('on')
            # 별이 스카이라인의 높이가 바뀌는 구간에 존재
            elif ans[k][0] == i[0]:
                if ans[k-1][1] > ans[k][1]:
                    if i[1] > ans[k-1][1]:
                        print('over')
                    elif ans[k][1] <= i[1] <= ans[k-1][1]:
                        print('on')
                    else:
                        print('under')
                else:
                    if i[1] < ans[k-1][1]:
                        print('under')
                    elif ans[k-1][1] <= i[1] <= ans[k][1]:
                        print('on')
                    else:
                        print('over')
            else:
                continue