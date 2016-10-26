
def merge(left, right):
    combined = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            combined.append(right.pop(0))
        else:
            combined.append(left.pop(0))
    while len(left) > 0:
        combined.append(left.pop(0))
    while len(right) > 0:
        combined.append(right.pop(0))
    return combined

'''
    This is a top down approach to the merge sort algorithm which recursively
    divides the input lists into smaller sublists that are then sorted and merge
    this is run back up the call chain from the base case.

    This implementation could be improved using deques because : list.pop(n) has a
    complexity of O(n) whereas list.popleft() is O(1) which is constant

    :param aList    list    A list of elements to sort that implement < operation

    :return list
'''
def sort(aList):
    size = len(aList)
    if size is 1 :
        return aList

    mid = size//2
    left = aList[:mid]
    right = aList[mid:]
    left = sort(left)
    right = sort(right)
    return merge(left, right)
