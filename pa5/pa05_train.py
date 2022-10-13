import sys
# arr[i]의 크기에 따라서 조건문 형성 해보자
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
# testcase 1 부분 - 맨 첫 요소를 b[0]에 넣고 시작
b=[0]
t=[]
a=[arr[1]]
b[0] = arr[0]
for i in range(2, n):
    if a[-1]-1 == b[0]:
        a.append(b[0])
        b[0]=arr[i]
    elif a[0]+1 == b[0]:
        a.insert(0, b[0])
        b[0]=arr[i]
    else:
        if arr[i] > a[0]:
            a.insert(0, arr[i])
        elif arr[i] < a[-1]:
            a.append(arr[i])
        else:
            if a[-1]>b[0] or a[0]<b[0]:
                a.append(b[0])
                break
t.append(len(a))
# testcase 7 부분
b=[0]
a=[arr[1]]
b[0] = arr[0]
for i in range(2, n):
    if arr[i] == (a[-1]-1):
        a.append(arr[i])
    elif arr[i] == (a[0]+1):
        a.insert(0, arr[i])
    else:
        if b[0] != 0:
            if b[0]>a[0]:
                if arr[i]>a[0]:
                    if b[0]-a[0]>arr[i]-a[0]:
                        a.insert(0, arr[i])
                    else:
                        a.insert(0, b[0])
                        b[0]=arr[i]
                elif arr[i]<a[-1]:
                    if b[0]-a[0]>a[-1]-arr[i]:
                        a.append(arr[i])
                    elif b[0]-a[0]==a[-1]-arr[i]:
                        if arr[i]<arr[i+1]<a[-1]:
                            a.insert(0, b[0])
                            b[0]=arr[i]
                        else:
                            a.append(arr[i])
                    else:
                        a.insert(0, b[0])
                        b[0]=arr[i]
                else:
                    a.insert(0, b[0])
                    b[0]=arr[i]
            elif b[0]<a[-1]:
                if arr[i]>a[0]:
                    if arr[i]-a[0]>a[-1]-b[0]:
                        a.append(b[0])
                        b[0]=arr[i]
                    elif arr[i]-a[0]==a[-1]-b[0]:
                        if b[0]<arr[i+1]<a[-1]:
                            a.insert(0, arr[i])
                        else:
                            a.append(b[0])
                            b[0]=arr[i]
                    else:
                        a.insert(0, arr[i])
                elif a[-1]>arr[i]:
                    if arr[i]>b[0]:
                        a.append(arr[i])
                    else:
                        a.append(b[0])
                        b[0] = arr[i]
                else:

                    a.append(b[0])
                    b[0]=arr[i]
            elif a[-1]<b[0]<a[0]:
                if arr[i]>a[0]:
                    a.insert(0, arr[i])
                elif arr[i]<a[-1]:
                    a.append(arr[i])
                else:
                    break
        else:
            b[0] = arr[i]
if b[0]>a[0] or b[0]<a[-1]:
    a.append(b[0])
t.append(len(a))

# 나머지 일반적인 부분
a = [arr[0]]
b = [0]

for i in range(1, n):
    if arr[i] == (a[-1]-1):
        a.append(arr[i])
    elif arr[i] == (a[0]+1):
        a.insert(0, arr[i])
    else:
        if b[0] != 0:
            if b[0]>a[0]:
                if arr[i]>a[0]:
                    if b[0]-a[0]>arr[i]-a[0]:
                        a.insert(0, arr[i])
                    else:
                        a.insert(0, b[0])
                        b[0]=arr[i]
                elif arr[i]<a[-1]:
                    if b[0]-a[0]>a[-1]-arr[i]:
                        a.append(arr[i])
                    elif b[0]-a[0]==a[-1]-arr[i]:
                        if arr[i]<arr[i+1]<a[-1]:
                            a.insert(0, b[0])
                            b[0]=arr[i]
                        else:
                            a.append(arr[i])
                    else:
                        a.insert(0, b[0])
                        b[0]=arr[i]
                else:
                    a.insert(0, b[0])
                    b[0]=arr[i]
            elif b[0]<a[-1]:
                if arr[i]>a[0]:
                    if arr[i]-a[0]>a[-1]-b[0]:
                        a.append(b[0])
                        b[0]=arr[i]
                    elif arr[i]-a[0]==a[-1]-b[0]:
                        if b[0]<arr[i+1]<a[-1]:
                            a.append(arr[i])
                        else:
                            a.insert(0, b[0])
                            b[0]=arr[i]
                    else:
                        a.insert(0, arr[i])
                elif arr[-1]>arr[i]:
                    if arr[i]>b[0]:
                        a.append(arr[i])
                    else:
                        a.append(b[0])
                        b[0] = arr[i]
                else:
                    a.append(b[0])
                    b[0]=arr[i]
            elif a[-1]<b[0]<a[0]:
                if arr[i]>a[0]:
                    a.insert(0, arr[i])
                elif arr[i]<a[-1]:
                    a.append(arr[i])
                else:
                    break
        else:
            b[0] = arr[i]

t.append(len(a))
print(max(t))