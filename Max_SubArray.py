
def find_cross_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    summation = 0
    max_left = 0
    max_right = 0
    for i in range(mid, low-1, -1):
        summation = summation + arr[i]
        if summation > left_sum:
            left_sum = summation
            max_left = i
    right_sum = float('-inf')
    summation = 0
    for j in range(mid+1, high+1):
        summation = summation + arr[j]
        if summation > right_sum:
            right_sum = summation
            max_right = j
    return left_sum+right_sum


def find_max_subarray(arr, low, high):
    if low == high:
        return arr[low]
    else:
        mid = int((low + high) / 2)
        (left_sum) = find_max_subarray(arr, low, mid)
        (right_sum) = find_max_subarray(arr, mid+1, high)
        (cross_sum) = find_cross_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum
        else:
            return cross_sum


a = [1, -10, 2, 5, 58, 78, -30, -5, 3, 1]
save = find_max_subarray(a, 0, len(a)-1)
print(save)

