n = int(input())
tmp_arr = []
arr = []
for i in range(n):
    tmp_arr.append(input().split())

for i in range(2):
    arr.append([tmp_arr[0][i]])

for i in range(1, n):
    for j in range(len(arr)):
        if tmp_arr[i][0] in arr[j]:
            if arr[-1] == arr[j]:
                arr.append([])
                arr[j+1].append(tmp_arr[i][1])
                break
            else:
                arr[j+1].append(tmp_arr[i][1])
                break

src = []
for i in range(2):
    src.append(input())
rlt = 0
for i in src:
    temp = 0
    for j in arr:
        if i in j:
            rlt = rlt + temp
            break
        else:
            temp += 1
if src[0] == src[1]:
    rlt = 0
print(rlt)