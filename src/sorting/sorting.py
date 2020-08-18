# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # this function merges two arrays that are already sorted (second half of process)
    elements = len(arrA) + len(arrB) #total number of elements 
    merged_arr = []

    a = 0
    b = 0 
    # Your code here
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    #need to see which array still has any elements left and push all of those elements 

    # for i in arrA:
    #     merged_arr.append(i)
    # for i in arrB:
    #     merged_arr.append(i)

    if a < len(arrA):
        merged_arr.extend(arrA[a:])
    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr

# arrA = [3, 6, 8, 12, 15]
# arrB = [5, 9, 18,19]
# print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # this function breaks array into two - passes them into merge() 
    if len(arr) > 1: 
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr

arr = [45, 12, 89, 14, 67, 45, 23, 90, 11]

print(merge_sort(arr))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
