def insertionsort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if(arr[i]<arr[j]):
                temp = arr[i]        #position of element is at j
                for idx in range(i,j,-1):
                    arr[idx]= arr[idx-1]
                arr[j]=temp
                break

    return arr

if __name__ == '__main__':
    arr = [10,51,2,18,4,31,13,5,23,64,29,8]
    sorted_arr = insertionsort(arr)
    print(sorted_arr)
