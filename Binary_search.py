def binary_search(arr, target):
    low =  0
    high = len(arr) -1
    while low <= high:
        mid = (low + high) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

arr =  [12,13,23,25,34,45,56,77]
target = 77

result = binary_search(arr, target)

if result != -1:
    print(f"element found at place {result+1}")
else:
    print("element not found")