'''
    Bubble Sort sorts elements in a list by swapping them in place one by one.
    So starting at element 0 in the list, check this against the rest of the list
    if anything in the list is smaller, then swap it with this element.
    i.e. 2 in 2, 3, 1, 4, 7 would be swapped with 1

    :param aList    list    The list of elements to sort

    :return list
'''
def sort(aList):
    for i in range(len(aList)):
        for j in range(i, len(aList)):
            if aList[i] > aList[j]:
                aList[i], aList[j] = aList[j], aList[i]
    return aList
