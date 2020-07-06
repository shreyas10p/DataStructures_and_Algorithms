def checkDiff(numList):
    total = 0
    first = 0
    second = 1
    while(second != len(numList)):
        if(numList[first] != numList[second]):
            total += abs(numList[second]-numList[first])-1
        first += 1
        second += 1
    return total

if __name__ == '__main__':
    testCase = input()
    for i in range(int(testCase)):
        numStr = int(input())
        numList = list(map(int,input().split()))
        res = checkDiff(numList)
        print(res)
