class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n_num1 = 0
        n_num2 = 0

        for i in range(len(num1)):
            n_num1 += (ord(num1[-i-1]) - 48) * 10**i

        for j in range(len(num2)):
            n_num2 += (ord(num2[-j-1]) - 48) * 10**j

        return str(n_num1*n_num2)


sol = Solution().multiply
a = sol("2", "3")
print(a)
b = sol("123", "456")
print(b)