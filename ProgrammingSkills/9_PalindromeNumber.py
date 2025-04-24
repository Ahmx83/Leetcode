class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        rev_x = x[::-1]

        return x == rev_x


sol = Solution().isPalindrome
a = sol(121)
print(a)