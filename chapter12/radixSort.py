import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) )+'/chapter8' )
import llistqueue
# sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) )+'/Chapter2' )
# from array import Array

def radixSort(theSeq):
    binArray = [None]*10
    for i in range(10):
        binArray[i] = llistqueue.Queue()

    seqLen = len(theSeq)
    maxVal = 0
    numDigit =0
    for x in theSeq:
        if(x>maxVal):
            maxVal = x

    while(maxVal!=0):
        maxVal = int(maxVal/10)
        numDigit += 1
    for j in range(numDigit):
        for num in theSeq:
            newNum = num/(10**j)
            digit = newNum%10
            binArray[digit].enqueue(num)
        newList = []
        for k in range(10):
            while not binArray[k].isEmpty():
                newList.append(binArray[k].dequeue())
        theSeq = newList

    return theSeq

if __name__ == '__main__':
    l = [23,10,18,51,5,13,31,54,48,62,29,8,2574]
    ans = radixSort(l)
    print(ans)
