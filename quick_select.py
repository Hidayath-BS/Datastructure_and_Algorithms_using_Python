import random
def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quickselect(arr, left, right, k):
    if left <= right:
        pivot_index = partition(arr, left, right)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickselect(arr,left,pivot_index -1, k)
        else:
            return quickselect(arr, pivot_index +1, right, k)
    return None

arr = [7,10,4,3,20,15]
k = 2
print(f"{k}th smallest element is", quickselect(arr, 0, len(arr)-1, k-1))