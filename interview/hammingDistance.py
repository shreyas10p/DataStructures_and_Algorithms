def hammingDistance(x,y):



class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        while(x > 0 or y > 0):
            if (((x & 1) and not (y & 1)) or (not (x & 1) and (y & 1))):
                count += 1

            x = x >> 1
            y = y >> 1

        return count

if __name__ == '__main__':
    solution = Solution()
    solution.hammingDistance(10,8)
