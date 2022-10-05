import sys
K, N = map(int, sys.stdin.readline().split())
arr = []
slot = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
for i in range(K):
    slot.append([0,0])

size = K
c = 0
for i in range(N):
    if arr[i] > 0 and c < size:
        for j in range(size):
            if slot[j][0] == 0:
                slot[j][0], slot[j][1] = j+1, arr[i]
                c = c+1
                break
    elif arr[i] > 0 and c == size:
        size = size*2
        for j in range(c, size):
            slot.append([0,0])
        slot[c][0], slot[c][1] = c+1, arr[i]
        c = c+1
    elif arr[i] < 0:
        a = abs(arr[i])
        for j in range(size):
            if slot[j][0] != 0 and slot[j][1] == a:
                slot[j][0], slot[j][1], c = 0, 0, c-1
                break
        if c <= size//3 and size != K:
            l = 1
            for x in range(size):
                if slot[x][0] != 0:
                    if x != l-1:
                        slot[l - 1][0], slot[l - 1][1], slot[x][0], slot[x][1] = l, slot[x][1], 0, 0
                    l = l+1
            del slot[size//2:]
            size = size//2

for i in range(size):
    if slot[i][0] != 0:
        print(slot[i][0], slot[i][1])
