def smallestVal(arr):
    n = len(arr)
    smallestNum = arr[0]
    for i in range(1,n):
        if(arr[i]<smallestNum):
            smallestNum = arr[i]
    return smallestNum

if __name__ == '__main__':
    arr = [2,3,4,12,43,21,1,0,-6,2,4,1,4]
    number = smallestVal(arr)
    print(number)
