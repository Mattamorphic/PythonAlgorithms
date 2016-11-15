def sort(aList):
    for i in range(0, len(aList)):
        # store current location
        index = i
        # store the current item
        item = aList[i]
        # iterate back through the list
        # and check item is less than the next item
        while index > 0  and item < aList[index - 1]:
            # move the item forward
            aList[index] = aList[index-1]
            # decrement the index
            index -=1
        # if we break the loop, this is where to insert
        aList[index] = item
    return aList
