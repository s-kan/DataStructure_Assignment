def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2

    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])

    a = []

    l = h = 0
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            a.append(low[l])
            l+=1
        else:
            a.append(high[h])
            h+=1
    a += low[l:]
    a += high[:h]
    return a