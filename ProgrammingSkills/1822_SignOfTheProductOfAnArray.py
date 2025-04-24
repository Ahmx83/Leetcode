class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        if 0 in nums:
            return 0

        def signFunc(x):
            hold = tuple(number for number in nums if number<0)
            if len(hold) % 2 == 1:
                return -1
            return 1
        return signFunc(nums)

print(list(filter(lambda x: x<0, [1, 4, -1, 4, -5])))