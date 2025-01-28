def kadane(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num,max_current + num)
        max_global = max(max_global, max_current)
    return max_global

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("maximum subarray sum", kadane(arr))
