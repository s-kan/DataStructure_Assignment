n = int(input())
# 입력부
arr = []
elements = []
dic_r = {}
dic_depth = {}

for i in range(n-1):
    r, h = input().split()
    elements.append(r)
    arr.append([r, h])

# 입력 받은 노드들을 key=parent, value=[childs] 형태로 딕셔너리에 넣는다
for i in arr:
    if i[1] in dic_r:
        dic_r[i[1]].append(i[0])
    else:
        dic_r[i[1]] = [i[0]]
for i in arr:
    if not i[0] in dic_r:
        dic_r[i[0]] = []

# 딕셔너리에서 root를 찾는다.
for i in dic_r:
    if not i in elements:
        root = i
        break

# 위에서 구한 root를 이용해 dic_r의 요소들을 key:depth, value:[nodes] 형태의 딕셔너리인 dic_depth에 넣는다
depth = 0
dic_depth[depth] = [root]
current = dic_r[root]
while(1):
    depth += 1
    dic_depth[depth] = []
    c = []
    for i in current:
        dic_depth[depth].append(i)
        for j in dic_r[i]:
            c.append(j)
    current = c
    if len(current) == 0:
        break

# dic_depth 의 depth가 가장 큰 노드들부터 시작해서 각 노드들의 subtree 개수를 구한다.
# result 딕셔너리는 key:node, value:# of subtree
# 자신의 child node들 각각의 subtree의 개수를 합하는 방식으로, depth가 가장 큰 node들 부터 올라가면서 구한다.
result = {}
for i in range(depth, -1, -1):
    for j in dic_depth[i]:
        result[j] = len(dic_r[j])
        for k in dic_r[j]:
            result[j] += result[k]
result = dict(sorted(result.items(), key=lambda x:x[1], reverse=True))

# result_arr 는 [node, # of subree, depth, subtree's depth] 가 요소인 2차원 배열
result_arr = []
for i in result:
    result_arr.append([i, result[i]])

# 각각의 depth를 구한다
for i in result_arr:
    for j in dic_depth:
        if i[0] in dic_depth[j]:
            i.append(j)

# 각각의 subtree's depth를 구한다
for i in result_arr:
    sub_depth = 0
    node = [i[0]]
    while(1):
        tmp_arr = []
        for j in node:
            for k in dic_r[j]:
                tmp_arr.append(k)
        node = tmp_arr
        sub_depth += 1
        if len(node) == 0:
            break
    i.append(sub_depth)

# 주어진 조건의 우선순위로 정렬한다.
result_arr = sorted(result_arr, key = lambda x:(-x[1], x[2], -x[3], x[0]))

for i in result_arr:
    print(i[0])