# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    start = 0
    end = len(arr) - 1
    found = False

    while start <= end and not found:
        midpoint = (start + end)//2
        if arr[midpoint] == target:
            found = True
        else:
            if target < arr[midpoint]:
                end = midpoint - 1
            else:
                start = midpoint + 1
    return found


arr1 = [2, 4, 3, 7, 6, 8, 1]
print(binary_search(arr1, 8, 0,  len(arr1) - 1))
