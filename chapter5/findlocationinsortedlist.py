#modified version of binary search to find the target location of the element in a sorted list
def findlocation(arr,ele):
    arrLen = len(arr)-1
    low = 0
    high = arrLen
    pos = "Not Found"
    while(low<=high):
        mid = (low+high)/2
        print(mid)
        if(arr[mid]>ele):
            high = mid-1
        elif(arr[mid]<ele):
            low = mid+1
        elif(arr[mid] == ele):
            pos = mid
            return pos
    return low
if __name__ == '__main__':
    arr = [1,10,20,25,30,40,50]
    position = findlocation(arr,5)
    print(position)
