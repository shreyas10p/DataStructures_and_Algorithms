def mergeVirtualSeq( theSeq, left, right, end, tmpArray ):
    a = left
    b = right
    m = 0
    while(a < right and b < end):
        if(theSeq[a] < theSeq[b]):
            tmpArray[m] = theSeq[a]
            a += 1
        else:
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1
    while(a < right):
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1
    while(b < end):
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1

    for i in range( end - left ):
        theSeq[i+left] = tmpArray[i]

    return theSeq

def recmergeSort(theSeq,first,last,tmpArray):
    if(first==last):
        return
    else:
        mid = int((first+last)/2)
        print(first,mid)
        recmergeSort(theSeq,first,mid,tmpArray)
        print(mid+1,last)
        recmergeSort(theSeq,mid+1,last,tmpArray)
        theSeq = mergeVirtualSeq(theSeq,first,mid+1,last+1,tmpArray)
        print(theSeq)
        return theSeq

if __name__ == '__main__':
    theSeq = [18,4,31]
    tmpArray = [None]*len(theSeq)
    seqLen = len(theSeq)-1
    ans = recmergeSort(theSeq,0,seqLen,tmpArray)
    print(ans)
