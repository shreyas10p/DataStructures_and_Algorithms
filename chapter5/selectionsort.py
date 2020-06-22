def selectionSort(arr):
    currentIdx = 0
    arrLen = len(arr)
    while(currentIdx<arrLen):
        smallest = arr[currentIdx]
        smallIdx = currentIdx
        for idx in range(currentIdx,arrLen):
            if(arr[idx]<arr[smallIdx]):
                smallIdx = idx

        temp = arr[currentIdx]
        arr[currentIdx] = arr[smallIdx]
        arr[smallIdx] = temp
        currentIdx += 1

    return arr



if __name__ == '__main__':
    arr = [2,8,1,29,43,41,28,47,89,98,0,24,28]
    sortedList = selectionSort(arr)
    print(sortedList)
