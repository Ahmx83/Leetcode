class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]
        """
        length = len(nums)
        #
        # for i in range(length):
        #     x = nums[i]
        #     for j in range(i+1, length):
        #         y = nums[j]
        #         if x + y == target:
        #             return [i, j]
        nums.sort()

        for i in range(length):
            x = nums[i]

            start = i + 1
            end = len(nums)
            while True:
                middle = end // 2 + 1

