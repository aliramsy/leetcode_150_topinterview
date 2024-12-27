class Solution:
    def removeDuplicates(self, nums: any) -> int:
        # nums = list(set(nums))
        nums[:] = [x for i, x in enumerate(nums) if i == 0 or x != nums[i - 1]]
        return len(nums)


solution = Solution()
print(solution.removeDuplicates([1,
                                 1, 2]))
