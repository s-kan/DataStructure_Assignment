import math

L1 = []
L2 = []

while (1):
    l1 = list(map(int, input().split()))
    if l1[0] == -9:
        break
    L1 = L1 + l1

while (1):
    l2 = list(map(int, input().split()))
    if l2[0] == -9:
        break
    L2 = L2 + l2

def shuffle(l):
    n1 = math.ceil(float(len(l))/2.0)
    n2 = len(l)-n1
    l1 = []
    l2 = []
    L=[]
    for i in range(n1):
        l1.append(l[i])
    for i in range(n1, n1+n2, 1):
        l2.append(l[i])
    if (n1>n2):
        for i in range(n2):
            L.append(l1[i])
            L.append(l2[i])
        L.append(l1[n1-1])
    else:
        for i in range(n2):
            L.append(l1[i])
            L.append(l2[i])
    return L

def distance(L1, L2):
    d=0
    l=L1
    while(1):
        l = shuffle(l)
        d = d+1
        if l==L2:
            return d
        elif L1 == l:
            return -1
        else:
            continue

dis = []
dis.append(distance(L1, L2))
dis.append(distance(L2, L1))
L0 = sorted(L1)

if distance(L0, L1) == -1 or distance(L0, L2) == -1:
    dis.append(-1)
else:
    dis.append(abs(distance(L0, L1)-distance(L0, L2)))

dis.sort()

for i in range(3):
    if dis[i] == -1:
        print("NOT")
        break
    else:
        print(dis[i])
        break
