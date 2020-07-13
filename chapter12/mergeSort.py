
def mergeDividedList(left,right):
    leftPointer = 0
    rightPointer = 0
    sortedList =[]
    while(leftPointer<len(left) and rightPointer<len(right)):
        if(left[leftPointer]>right[rightPointer]):

            sortedList.append(right[rightPointer])
            rightPointer += 1
        elif(left[leftPointer]<right[rightPointer]):
            sortedList.append(left[leftPointer])
            leftPointer += 1
        else:
            sortedList.append(left[leftPointer])
            sortedList.append(right[rightPointer])
            rightPointer += 1
            leftPointer += 1
    while (leftPointer<len(left)):
        sortedList.append(left[leftPointer])
        leftPointer += 1
    while (rightPointer<len(right)):
        sortedList.append(right[rightPointer])
        rightPointer += 1
    return sortedList

def mergeSort(theList):
    arrayLen = len(theList)
    if(arrayLen<=1):
        return theList
    else:
        mid = int(arrayLen /2)
        leftHalf = mergeSort(theList[:mid])
        rightHalf = mergeSort(theList[mid:])
        if(leftHalf is not None or rightHalf is not None):
            newList = mergeDividedList(leftHalf,rightHalf)
        return newList
if __name__ == '__main__':
    x = [10,23,51,18,4,31,13,5,1]
    a =mergeSort(x)
    print(a)
