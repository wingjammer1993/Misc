def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)
    print(arr)


def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if j <= r-1:
            if arr[j] <= pivot:
                i = i+1
                # swap
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    i = i + 1
    # swap
    temp = arr[i]
    arr[i] = pivot
    arr[r] = temp
    pivot_index = arr.index(pivot)
    return pivot_index


a = [10, 2, 5, 3, 7, 13, 1, 6]
quick_sort(a, 0, len(a)-1)

