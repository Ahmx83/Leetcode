class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: list[int]
        :rtype: list[int]
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        digits.insert(0, 0)
        digits[-1] += 1

        for i in range(1, len(digits)):
            i = -i
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
                carry = 1

        if digits[0] == 0:
            digits.remove(0)
        return digits


a = Solution()
b = a.plusOne([9, 9, 9])
print(b)
