class Solution:
    def removeDuplicates(self, nums: any) -> int:
        nums[:] = [num for i, num in enumerate(
            nums) if i == 0 or i == 1 or num != nums[i-1] or num != nums[i-2]]
