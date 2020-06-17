# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    if len(arrA) or len(arrB) < 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # split list into 2 halves
    if len(arr) == 1
    return arr
    left_array = []
    right_array = []
    # further split up first half
    # further split up until only 1 in each array for first array
    # recursively merge adjacent partitions
    # for i = leftpart_index to rightpart_index
    # if leftpart_headvalue <= rightpart_headvalue
    # copy leftpart_headvalue
    # else: copy rightpart_headvalue
    # copy elements back to the original array

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

    # from python quick sort algorithm video: https://www.youtube.com/watch?v=CB_NCoxzQnk


def quick_sort(A):
    qick_sort2(A, 0, len(A) - 1)


def quick_sort2(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)
        quick_sort2(A, low, p-1
                    quick_sort2(A, p + 1, hi))
