class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: list[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if j != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums