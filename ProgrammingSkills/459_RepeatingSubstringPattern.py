class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        maxNumOfLetters = len(s) // 2
        lengthOfWord = len(s)
        for numOfSubstrings in range(maxNumOfLetters, 0, -1):
            if lengthOfWord % numOfSubstrings != 0:
                continue
            toCompare = []
            numOfSegments = int(lengthOfWord / numOfSubstrings)
            for nthSegment in range(numOfSegments):
                toCompare.append(s[numOfSubstrings * nthSegment:
                                   numOfSubstrings + (numOfSubstrings * nthSegment)])
            cool = None
            for match in toCompare:
                if match != toCompare[0]:
                    cool = False
            if cool is None:
                return True
        return False



# a = Solution().repeatedSubstringPattern('abac')
# print(a)
# b = Solution().repeatedSubstringPattern('aba')
# print(b)
# c = Solution().repeatedSubstringPattern('bb')
# print(c)
# d = Solution().repeatedSubstringPattern('ababba')
# print(d)
# e = Solution().repeatedSubstringPattern('zzz')
# print(e)

# s = 'abcabcabc'
# print((s*2)[1:-1])
