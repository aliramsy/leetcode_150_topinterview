class Solution:
    def canJump(self, nums: any) -> bool:
        result = True
        length = len(nums)
        cursor = 0
        for i, num in enumerate(nums):
            if i == length - 1:
                return True
            else:
                if num > cursor:
                    cursor = num
                cursor = cursor - 1
                if cursor < 0:
                    result = False
                    break
        return result


solution = Solution()
print(solution.canJump([3, 2, 1, 0, 4]))
