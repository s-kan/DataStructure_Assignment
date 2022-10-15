N = int(input())
lst = [int(input()) for _ in range(N)]
answer = 0

def dfs(idx, station, trains):
    global answer
    if idx == N:
        if station:
            if station > trains[0]:
                trains = [station] + trains
            elif station < trains[-1]:
                trains = trains + [station]

        answer = max(answer, len(trains))
        return

    next_train = lst[idx]

    if station:
        if trains[0] + 1 == station:
            dfs(idx , 0, [station] + trains)

        elif trains[-1] - 1 == station:
            dfs(idx , 0, trains + [station])

    if trains[0] + 1 == next_train:
        dfs(idx + 1, station, [next_train] + trains)

    elif trains[-1] - 1 == next_train:
        dfs(idx + 1, station, trains + [next_train])

    else:
        if not station:
            dfs(idx + 1, next_train, trains)
            if next_train > trains[0]:
                dfs(idx + 1, 0, [next_train] + trains)

            elif next_train < trains[-1]:
                dfs(idx + 1, 0, trains + [next_train])

        else:
            flag1, flag2 = 0, 0
            if station > trains[0]:
                dfs(idx , 0, [station] + trains)
            elif station < trains[-1]:
                dfs(idx , 0, trains + [station])
            else:
                flag1 = 1


            if next_train > trains[0]:
                dfs(idx + 1, station, [next_train] + trains)

            elif next_train < trains[-1]:
                dfs(idx + 1, station, trains + [next_train])
            else:
                flag2 = 1

            if flag1 and flag2:
                answer = max(answer, len(trains))
                return



dfs(1, 0, [lst[0]])
dfs(2, lst[0], [lst[1]])

print(answer)