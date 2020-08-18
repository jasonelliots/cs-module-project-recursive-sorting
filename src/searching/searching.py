# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    #condition to check that you haven't searched the whole array
    if end >= start:
        #set up midpoint
        midpoint = (start + end) // 2
        #condition to check if the midpoint is the target
        if arr[midpoint] == target:
            return midpoint 
        #condition to check if target is less than value at midpoint - recursion on left side of tree
        elif target < arr[midpoint]:
            return binary_search(arr, target, start, midpoint-1)
        #else (target is greater than midpoint) - recursion on right side of tree 
        else:
            return binary_search(arr, target, midpoint+1, end)
    #else target not found 
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass 
