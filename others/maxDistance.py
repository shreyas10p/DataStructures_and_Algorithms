class Solution:
    def maxDistToClosest(self, seats) -> int:
        A = 0
        B = 1
        distance = 0
        seatsLen = len(seats)
        for idx in range(1,seatsLen):
            if((seats[idx]==1) or (idx == (seatsLen-1))):
                if(seats[B] == 1):
                    A = B
                B = idx

                if(seats[A] == 1 and seats[B] == 1):
                    if(distance < (B-A)//2):
                        distance = (B-A)//2
                    if(A==B):
                        distance =1
                else:
                    if(distance<(B-A)):
                        distance = B-A

        return distance

if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxDistToClosest([0,1])
    print(ans)
