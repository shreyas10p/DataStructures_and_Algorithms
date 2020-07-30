class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for num in range(1,N+1):
            print(num)
            if(self.checkGoodNum(num)):
                count+=1
        return count

    def checkGoodNum(self,num: int) -> bool:
        goodNum = [2,5,6,9]
        while(num>0):
            if((num%10) not in goodNum):
                return False
            else:
                num=num//10
        return True

if __name__ == '__main__':
    solution = Solution()
    ans = solution.rotatedDigits(10)
    print(ans)
