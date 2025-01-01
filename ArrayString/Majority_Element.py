class Solution:
    def majorityElement(self, nums: any) -> int:
        nums[:] = sorted(nums)
        k = 0
        length = len(nums)
        for i, num in enumerate(nums):
            if length == 1:
                return num
            else:
                if i == 0:
                    k = 1
                elif num != nums[i-1]:
                    k = 1
                else:
                    k += 1
                    if k > length // 2:
                        return num


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
