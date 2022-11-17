n = int(input())

arr = []
elements = []
dic_r = {}
dic_depth = {}

for i in range(n-1):
    r, h = input().split()
    elements.append(r)
    arr.append([r, h])

for i in arr:
    if i[1] in dic_r:
        dic_r[i[1]].append(i[0])
    else:
        dic_r[i[1]] = [i[0]]
for i in arr:
    if not i[0] in dic_r:
        dic_r[i[0]] = []

for i in dic_r:
    if not i in elements:
        root = i
        break

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


result = {}
for i in range(depth, -1, -1):
    for j in dic_depth[i]:
        result[j] = len(dic_r[j])
        for k in dic_r[j]:
            result[j] += result[k]
result = dict(sorted(result.items(), key=lambda x:x[1], reverse=True))

result_arr = []
for i in result:
    result_arr.append([i, result[i]])

for i in result_arr:
    for j in dic_depth:
        if i[0] in dic_depth[j]:
            i.append(j)

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


result_arr = sorted(result_arr, key = lambda x:(-x[1], x[2], -x[3], x[0]))

for i in result_arr:
    print(i[0])