def quickSort(array,first,last):
    if(first>=last):
        return
    array,pivotIdx = rearrange(array,first,last)
    quickSort(array,pivotIdx+1,last)
    quickSort(array,first,pivotIdx-1)
    return array

def rearrange(array,first,last):

    pivot = array[first]
    left = first + 1
    right = last
    while left <= right :

        while left < right and array[left] < pivot :
            left += 1

        while right >= left and array[right] >= pivot :
            right -= 1

        if left < right :
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp

    if right != first :
        array[first] = array[right]
        array[right] = pivot

    return array,right

if __name__ == '__main__':
    arr = [10,23,51,18,4,31,5,13]
    last = len(arr)-1
    newList = quickSort(arr,0,last)
    print(newList)
