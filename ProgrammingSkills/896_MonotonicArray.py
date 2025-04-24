class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: list[int]
        :rtype: bool
        """
        mode = None
        i = 0
        while mode is None:
            try:
                if nums[i] < nums[i+1]:
                    mode = True
                elif nums[i] > nums[i+1]:
                    mode = False
                i += 1
            except IndexError:
                return True
        print(mode)
        if mode is True:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
        else:
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
        return True


a = Solution()
b = a.isMonotonic([1,1,2])
print(b)