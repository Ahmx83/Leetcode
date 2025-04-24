class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a, b = max(a, b, key=len), min(b, a, key=len)
        b = b.rjust(len(a), "0")

        carry = ["0"]
        result = []
        # print(a, b)
        for i in range(-1, -len(a)-1, -1):
            x = a[i]
            y = b[i]
            # print(x, y)

            if x == "0" and y == '0':
                result.append("0")
                carry.append("0")
            elif x == "1" and y == "1":
                result.append("0")
                carry.append("1")
            else:
                result.append("1")
                carry.append("0")

        result = "".join(reversed(result))

        if "1" in carry:
            carry = "".join(reversed(carry))
            return self.addBinary(result, carry).lstrip("0")
        return result

sol = Solution().addBinary
c = sol("1010", "1011")
print(c)