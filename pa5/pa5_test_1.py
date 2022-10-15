import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
t=[]
b=arr[0]
a=[arr[1]]

for i in range(2, n):
    if b<a[-1]:
        if a[-1]-1==b or arr[i]<b:
            a.append(b)
            b = arr[i]
        elif a[0]<arr[i]:
            a.insert(0, arr[i])
        elif b<arr[i]<a[-1]:
            a.append(arr[i])
    elif a[0]<b:
        if a[0]+1==b or b<arr[i]:
            a.insert(0, b)
            b = arr[i]
        elif arr[i]<a[-1]:
            a.append(arr[i])
        elif a[0]<arr[i]<b:
            a.insert(0, arr[i])
    else:
        if arr[i]<a[-1]:
            a.append(arr[i])
        elif a[0]<arr[i]:
            a.insert(0, arr[i])
        else:
            break
if b<a[-1]:
    a.append(b)
elif a[0]<a[0]:
    a.insert(0, b)
print(a)
print(len(a))
t.append(len(a))

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
print(a)
t.append(len(a))
print(max(t))