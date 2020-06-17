# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
#     if len(arrA) or len(arrB) < 1

#     return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(mainlist):
    print("split list", mainlist)
    # base case

    if len(mainlist) > 1:
        mid = len(mainlist)//2
        lefthalf = mainlist[:mid]
        righthalf = mainlist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        a = 0  # lefthalf starting index
        b = 0  # righthalf starting index
        c = 0  # mainlist starting index
        while a < len(lefthalf) and b < len(righthalf):
            if lefthalf[a] <= righthalf[b]:
                mainlist[c] = lefthalf[a]
                a = a + 1
            else:
                mainlist[c] = righthalf[b]
                b = b + 1
            c = c + 1

        while a < len(lefthalf):
            mainlist[c] = lefthalf[a]
            a = a + 1
            c = c + 1
        while b < len(righthalf):
            mainlist[c] = righthalf[b]
            b = b + 1
            c = c + 1
    print("merging to main list", mainlist)


mainlist = [5, 7, 2, 3, 9, 1, 4, 0]
merge_sort(mainlist)
print(mainlist)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

#     # from python quick sort algorithm video: https://www.youtube.com/watch?v=CB_NCoxzQnk


# def quick_sort(A):
#     qick_sort2(A, 0, len(A) - 1)


# def quick_sort2(A, low, hi):
#     if low < hi:
#         p = partition(A, low, hi)
#         quick_sort2(A, low, p-1
#                     quick_sort2(A, p + 1, hi))
