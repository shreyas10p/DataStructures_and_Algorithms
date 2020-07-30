def reverse(string):
    stringLen = len(string)
    newString = ""
    for i in range(stringLen-1,-1,-1):
        newString += ""+string[i]
    return newString

def find_missing(listA,listB):
    xorSum = 0
    for num in listA:
        xorSum ^= num
        print(xorSum)
    for num in listB:
        xorSum ^= num

    return xorSum

# If we find xor of a number and then again xor the number it undoes the effect of number.
if __name__ == '__main__':
    x = reverse('shreyas')
    print(x)
    A= [4,12,9,5,6]
    B = [4,12,9,6]
    ans = find_missing(A,B)
    print(ans)
