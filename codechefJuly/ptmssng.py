# from collections import defaultdict

def findOddNum(Map):
    for key,val in Map.items():
        if(val%2 != 0):
            return key

if __name__ == '__main__':
    testCase = input()
    countMapX = {}
    countMapY = {}
    for i in range(int(testCase)):
        num = int(input())
        for j in range(4*num):
            x,y = map(int,input().split())
            if(x not in countMapX):
                countMapX[x] = 1
            else:
                countMapX[x] += 1
            if(y not in countMapY):
                countMapY[y] = 1
            else:
                countMapY[y] += 1
        resX = findOddNum(countMapX)
        resY = findOddNum(countMapY)
        print(resX,end=" ")
        print(resY)
