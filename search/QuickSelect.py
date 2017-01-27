'''
    Implementation of Quick Select.
    This will return the kth smallest number in a list of numbers
    We use a similar process to the binary search divide and conquer algorithm
    We choose a pivot value from the list, and partition the list into that which
    is smaller than the pivot, and that which is greater.
    If the pivot value is our value, then stop
    If the length of the smaller left side is greater than or equal to k, then recursively hunt the left partition
    If the length of the smaller left side is less than k-1 then, the item must be the right size, however we need to
        update k in relation to this partion (so we minus from k, the size of the left part we're throwing away and 1 for the pivot)

    :param integer      k       The kth smallest item in the list we want
    :aList list(int)    aList   A List of integers 
'''
def search(k, aList):
    if len(aList) == 1:
        return aList[0]
    pivotValue = aList[0]
    leftPart = list()
    rightPart = list()
    for i in aList[1:]:
        leftPart.append(i) if i < pivotValue else rightPart.append(i)
    if len(leftPart) >= k:
        return search(k, leftPart)
    elif len(leftPart) == (k - 1):
        return pivotValue
    else:
        return search(k-len(leftPart)-1, rightPart)
