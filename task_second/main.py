
def upper_bound_binary_search(arr,target):
    low = 0
    high = len(arr) - 1
    mid = 0
    itterations = 0
    candidate = None
    while low <= high:
        itterations +=1
        mid = (low + high) // 2
        if arr[mid] >= target:
            candidate = arr[mid]
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
    return (itterations, candidate)

arr = [1, 3, 5, 7, 9]
target = 6

a = upper_bound_binary_search(arr,target)
print(a)