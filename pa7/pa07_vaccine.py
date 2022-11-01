n = int(input())

c = []
o_m = []
o_f = []
a_m = []
a_f = []

for i in range(n):
    arr = list(input().split())
    if int(arr[1])<=15:
        c.append(arr)
    elif 16<=int(arr[1])<=60:
        if arr[2] == 'M':
            a_m.append(arr)
        else:
            a_f.append(arr)
    else:
        if arr[2] == 'M':
            o_m.append(arr)
        else:
            o_f.append(arr)

for i in o_m:
    print(i[0])
for i in o_f:
    print(i[0])
for i in c:
    print(i[0])
for i in a_f:
    print(i[0])
for i in a_m:
    print(i[0])