import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from Chapter2.array import Array
class MaxHeap(object):
    """docstring for MaxHeap"""
    def __init__(self, maxSize):
        self._heap = Array(maxSize)
        self._index = 0

    def __len__(self):
        return self._index

    def capacity(self):
        return len(self._heap)

    def add(self,value):
        assert self.capacity()>self._index,"Cannot add to heap"
        self._heap[self._index] = value
        self._index +=1
        self._siftUp(self._index -1)

    def extract(self):
        assert self._index >0 ,"cannot extract from empty heap"
        value = self._heap[0]
        self._index -= 1
        self._heap[0] = self._heap[self._index]
        self._heap[self._index] = None
        self._siftDown(0)
        return value

    def _siftUp(self,idx):
        if(idx>0):
            parentIdx = (idx - 1)//2
            if(self._heap[idx]>self._heap[parentIdx]):
                parentVal = self._heap[parentIdx]
                self._heap[parentIdx] = self._heap[idx]
                self._heap[idx] = parentVal
                self._siftUp(parentIdx)

    def _siftDown( self, ndx ):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        largest = ndx
        if left < self._index and self._heap[left] >= self._heap[largest] :
            largest = left
        #Resolved error in the book
        if right < self._index and self._heap[right] >= self._heap[largest]:

            largest = right
        if largest != ndx :
            temp =  self._heap[largest]
            self._heap[largest] = self._heap[ndx]
            self._heap[ndx] = temp
            self._siftDown( largest )

# if __name__ == '__main__':
#     heap = MaxHeap(10)
#     heap.add(100)
#     heap.add(71)
#     heap.add(84)
#     heap.add(14)
#     heap.add(91)
#     heap.add(50)
#     heap.add(62)
#     heap.add(89)
#     heap.add(10)
#     heap.add(7)
#     heap.extract()
#     print(heap._heap)
#     for num in range(10):
#         print(heap._heap[num])
