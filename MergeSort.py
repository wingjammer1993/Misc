#!/bin/python3


def merge_sort(arr, p, q):
    if p < q:
        mid = int((p+q)/2)
        merge_sort(arr, p, mid)
        merge_sort(arr, mid+1, q)
        merge(arr, p, mid, q)


def merge(arr, p, mid, q):
    n1 = mid-p+1
    n2 = q - mid
    lefty = [0]*n1
    righty = [0]*n2
    for x in range(0, n1):
        lefty[x] = arr[p + x]
    for x in range(0, n2):
        righty[x] = arr[mid + x + 1]
    lefty.append(float('inf'))
    righty.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, q+1):
        if lefty[i] <= righty[j]:
            arr[k] = lefty[i]
            i = i + 1
        else:
            arr[k] = righty[j]
            j = j + 1
    print(arr)


a = [10, 2, 5, 3, 7, 13, 1, 6]
merge_sort(a, 0, len(a)-1)

