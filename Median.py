def median_stats(arr, p, r, i):

    # If p == r, simply return
    if p == r:
        return arr[p]

    # else, take one pass of partition
    q = partition(arr, p, r)

    # find out which order of input array you just found with the partition
    k = q - p + 1

    # if that order is same as required, return
    if i == k:
        return arr[q]

    # if it is less, retain first partition and search in it
    elif i < k:
        return median_stats(arr, p, q-1, i)

    # else, search in second partition for i-k th order, since the array is partitioned.
    else:
        return median_stats(arr, q+1, r, i-k)


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
save = median_stats(a, 0, len(a)-1, 4)
print(save)

