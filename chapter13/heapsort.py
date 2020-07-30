from maxHeap import MaxHeap

def heapSort(nums):

    size = len(unsorted_array)
    heap = MaxHeap(size)
    sorted_array = []
    for i in range(size):
        heap.add(unsorted_array[i])
    for j in range(size):
        for i in range(size):
        sorted_array.append(heap.extract())
    return sorted_array

if __name__ == '__main__':
    unsorted_array = [9,45,36,87,89,2,3,56,77,55,10]
    print(heapSort(unsorted_array))
