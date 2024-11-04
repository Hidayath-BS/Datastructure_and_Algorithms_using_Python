def liner_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    else:
        return -1
    
arr = [12,13,31,43,56]
target = 43

value = liner_search(arr, target)

if value != -1:
    print(f"element found at place {value + 1}")
else:
    print("element not present")
