N = int(input())
lst = [int(input()) for _ in range(N)]

answer = 0

# index, 계류장 상태, 기차
def dfs(idx, station, trains):
    global answer

    # index가 N까지 도달 했으면
    if idx == N:

        # 계류장에 기차가 남아있을 경우, 계류장에 있는 기차를 배열에 붙일 수 있는 지 확인하고, 배열에 붙인다.
        if station:
            if station > trains[0]:
                trains = [station] + trains
            elif station < trains[-1]:
                trains = trains + [station]

        # 기차 배열의 크기가 정답보다 크다면, 정답을 갱신해준다.
        answer = max(answer, len(trains))
        return

    # 다음 기차 = lst[idx]
    next_train = lst[idx]

    # 임시계류장에 기차가 있을 경우, 임시계류장의 기차가 기차배열의 양쪽에 붙일 수 있는지 확인하고,
    # 붙일 수 있다면 임시계류장의 기차를 붙이고, 임시계류장은 비워준다.
    # 아직 다음 기차로는 안넘어갔기 때문에, idx는 그대로다.
    if station:
        if trains[0] + 1 == station:
            dfs(idx , 0, [station] + trains)

        elif trains[-1] - 1 == station:
            dfs(idx , 0, trains + [station])


    # 만약 다음 기차가, 기차배열의 양쪽에 붙는 기차라면, 기차배열에 붙여주고, 임시계류장의 상태는 그대로 유지하고,
    # idx는 1 증가시킨다.
    if trains[0] + 1 == next_train:
        dfs(idx + 1, station, [next_train] + trains)

    elif trains[-1] - 1 == next_train:
        dfs(idx + 1, station, trains + [next_train])

    # 만약 다음 기차가 기차배열의 양쪽의 +- 1 이 아니라면,
    else:
        if not station: # 임시계류장에 아무것도 없을 때는,
            dfs(idx + 1, next_train, trains) # 임시계류장에 다음 기차를 넣어주고, idx를 1 증가시킨다.

            # 다음기차가 기차배열의 +-1이 아님에도 불구하고, 임시계류장에 넣지 않고 그냥 기차배열에 붙이고 싶다면,
            # 다음 기차의 범위가 기차배열에 붙일 수 있는 범위인지 (즉, 기차배열이 [5, 30] 이고, 다음 기차가 2나 32면 붙일 수 있는데, 24면 못 붙임)
            # 확인하고, 기차배열에 붙인다.
            # 계류장에 아무것도 없으니까, 값은 0이다.
            if next_train > trains[0]:
                dfs(idx + 1, 0, [next_train] + trains)

            elif next_train < trains[-1]:
                dfs(idx + 1, 0, trains + [next_train])

        # 임시계류장에 기차가 이미 있는 경우
        else:
            # 1. 임시계류장에서 내리기
            # 2. 그냥 갖다 붙이기
            # 만약, 임시계류장에 기차가 있는 상태인데, 다음 기차를 기차배열에 붙일 수 없다면, return 해야 한다.

            flag1, flag2 = 0, 0

            # 임시계류장의 기차가, 기차배열에 붙을 수 있다면, 기차배열에 붙이고 임시계류장은 0으로 초기화한다.
            # 다음기차는 아직 건들지 않았으므로, idx는 그대로다.
            if station > trains[0]:
                dfs(idx , 0, [station] + trains)
            elif station < trains[-1]:
                dfs(idx , 0, trains + [station])

            # 만약 계류장의 기차를 기차배열에 붙일 수 없다면, flag1을 1로 설정한다.
            else:
                flag1 = 1


            # 다음 기차가 기차배열에 붙을 수 있는지 확인하고, 붙을 수 있다면 기차배열에 붙인다.
            if next_train > trains[0]:
                dfs(idx + 1, station, [next_train] + trains)

            elif next_train < trains[-1]:
                dfs(idx + 1, station, trains + [next_train])

            # 다음 기차가 기차배열에 붙을 수 없다면, flag2를 1로 설정한다.
            else:
                flag2 = 1


            # 계류장의 기차도 붙일 수 없고, 다음 기차도 붙일 수 없으므로, answer를 갱신해주고, return한다.
            # 예를 들어, 계류장에 기차가 7이 있고, 기차배열에는 [2, 3, 4, 5, 8]이 있고, 다음 기차가 6이라면,
            # 계류장의 기차도 못붙이고, 다음 기차도 못붙인다.
            if flag1 and flag2:
                answer = max(answer, len(trains))
                return



# (기차를 N칸 모두 붙일 수도 있고, 못 붙일 수도 있음을 참고)
# 첫 기차를 임시계류장에 안 넣는 경우
dfs(1, 0, [lst[0]])

# 첫 기차를 임시계류장에 넣는 경우
dfs(2, lst[0], [lst[1]])

print(answer)