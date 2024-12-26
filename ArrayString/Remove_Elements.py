class Solution:
    def removeElement(self, nums: any, val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return len(nums)


solution = Solution()
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
