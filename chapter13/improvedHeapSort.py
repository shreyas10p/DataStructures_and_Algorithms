# Improved Max Heap algorithm for space complexity

def improvedHeapSort(theSeq):
    theSeqLen = len(theSeq)
    for index in range(1,theSeqLen):
        siftUp(theSeq,index)
    for index in range(1,theSeqLen):
        topEle = theSeq[0]
        theSeq[0] = theSeq[theSeqLen-index]
        theSeq[theSeqLen-index] = topEle
        siftDown(theSeq,0,theSeqLen-index)
    return theSeq


def siftUp(theSeq,idx):
    if(idx>0):
        parentIdx = (idx-1)//2
        if(theSeq[idx]>theSeq[parentIdx]):
            temp =  theSeq[parentIdx]
            theSeq[parentIdx] = theSeq[idx]
            theSeq[idx] = temp
            siftUp(theSeq,parentIdx)
    print(theSeq)
    return theSeq

def siftDown(theSeq,idx,lastIndex):
    left = (2*idx +1)
    right = (2*idx+2)
    largest = idx
    if(left<lastIndex and theSeq[left]>theSeq[largest] ):
        largest = left
    if(right<lastIndex and theSeq[right]>theSeq[largest]):
        largest = right

    if(largest != idx):
        temp = theSeq[largest]
        theSeq[largest] = theSeq[idx]
        theSeq[idx] = temp
        siftDown(theSeq,largest,lastIndex)
    return theSeq

if __name__ == '__main__':
    sequence = [10,51,2,18,4,31,13,5,23,64,29]
    print(improvedHeapSort(sequence))
