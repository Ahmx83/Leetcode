class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = dict(
            I = 1,
            V = 5,
            X = 10,
            L = 50,
            C = 100,
            D = 500,
            M = 1000
        )
        total = 0
        digit_current = 0
        i = -1
        for _ in range(len(s)):
            numeral_current = 0
            digit_current = 0
            numeral_next = 0
            digit_next = 0
            try:
                numeral_current = s[i]
                digit_current = roman_to_int[numeral_current]
                numeral_next    = s[i-1]
                digit_next    = roman_to_int[numeral_next]
            except KeyError:
                total += digit_current
                break
            except IndexError:
                total += digit_current
                break

            i -= 1
            if digit_current > digit_next:
                total += digit_current - digit_next
                i -= 1
            else:
                total += digit_current

        return total


# S = Solution()
# a = S.romanToInt('III')
# print(a)
# b = S.romanToInt('MCMXCIV')
# print(b)
# c = S.romanToInt('IV')
# print(c)
