'''
    Selectuib Sort sorts elements in a list by moving the largest element to the
    end of the list in each pass, then moving the fill space back one, so on the first pass of

    [3, 12, 5, 8, 23, 9]

    would result in

    [3, 12, 5, 8, 9, 23]

    then

    [3, 9, 5, 8, 12, 23]

    :param aList    list    The list of elements to sort

    :return list
'''
def sort(aList):
    for fill in range(len(aList)-1, 0, -1):
        max_index=0
        for index in range(1, fill+1):
            if aList[index] > aList[max_index]:
                max_index = index
        aList[fill], aList[max_index] = aList[max_index], aList[fill]
    return aList
