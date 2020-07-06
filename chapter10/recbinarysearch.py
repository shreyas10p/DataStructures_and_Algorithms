def revBinarySearch(target,theSeq,first,last):
    if(first>last):
        return False
    else:
        mid = int((first+last)/2)
        if(theSeq[mid] == target):
            return mid
        elif(theSeq[mid]>target):
            last = mid
            return revBinarySearch(target,theSeq,first,last)
        elif(theSeq[mid]<target):
            first = mid
            return revBinarySearch(target,theSeq,first,last)

if __name__ == '__main__':
    sequence = [7,10,19,29,39,99,500,501,560]
    ele = revBinarySearch(501,sequence,0,len(sequence)-1)
    print(ele)
