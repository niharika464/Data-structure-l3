def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid -1)
    else:
        return binary_search(arr, target,low, high)
    
arr = [2, 4, 6, 8, 9]
print(binary_search(arr, 1, 0,len(arr) -1))    