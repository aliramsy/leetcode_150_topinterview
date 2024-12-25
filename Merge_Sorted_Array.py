class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        [nums1.append(i) for i in nums2]
        nums1[:] = sorted(nums1)
        # nums1[:] = sorted(nums1[:m] + nums2[])


solution = Solution()
solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6],  3)
