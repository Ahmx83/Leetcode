class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        z = (high - low) // 2 + (high - low) % 2
        if low % 2 == 0 or high % 2 == 0:
            return z
        else:
            return z + 1



sol = Solution()
a = sol.countOdds(8, 10)
print(a)