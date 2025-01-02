class Solution:
    def rotate(self, nums: any, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[length - k:] + nums[:length - k]
        return nums


solution = Solution()
print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 7))
