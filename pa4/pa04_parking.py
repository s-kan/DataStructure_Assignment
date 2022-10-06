import sys

K, N = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
slot = [0]*K

size = K
c = 0
for i in range(N):
    if arr[i] > 0:
        if c != size:
            slot[slot.index(0)] = arr[i]
            c = c+1
        else:
            size = size * 2
            slot.extend([0]*size)
            slot[c] = arr[i]
            c = c + 1
    elif arr[i] < 0:
        a = abs(arr[i])
        for j in range(size):
            if slot[j] != 0 and slot[j] == a:
                slot[j], c = 0, c-1
                break
        if c <= size//3 and size != K:
            l = 1
            for x in range(size):
                if slot[x] != 0:
                    if x != l-1:
                        slot[l - 1], slot[x] = slot[x], 0
                    l = l+1
            del slot[size//2:]
            size = size//2

for i in range(size):
    if slot[i] != 0:
        print(i+1, slot[i])
