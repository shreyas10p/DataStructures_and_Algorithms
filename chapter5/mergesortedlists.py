def mergeSortedLists(listA,listB):
    idxA = 0
    idxB = 0
    mergeList = []
    while(idxA<(len(listA)) and idxB<(len(listB))):
        if(listA[idxA]>listB[idxB]):
            mergeList.append(listB[idxB])
            idxB += 1
        elif(listA[idxA]<listB[idxB]):
            mergeList.append(listA[idxA])
            idxA += 1
        elif(listA[idxA]==listB[idxB]):
            mergeList.append(listA[idxA])
            idxA += 1
            mergeList.append(listB[idxB])
            idxB += 1

    # If listA contains more items, append them to newList.
    while idxA < len( listA ) :
        mergeList.append( listA[idxA] )
        idxA += 1
    # Or if listB contains more items, append them to newList.
    while idxB < len( listB ) :
        mergeList.append( listB[idxB] )
        idxB += 1
    return mergeList



if __name__ == '__main__':
    listA = [2,8,15,23,30]
    listB = [4,13,24,34]
    mergedList = mergeSortedLists(listA,listB)
    print(mergedList)
