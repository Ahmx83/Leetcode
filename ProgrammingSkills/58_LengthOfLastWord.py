class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        start_index = -1
        while True:
            try:
                if s[start_index] == " ":
                    start_index += 1
                    break
            except IndexError:
                return len(s)
            start_index -= 1

        word_len = len(s[start_index:])
        return word_len


a = Solution()
b = a.lengthOfLastWord("   fly me   to   the moon  ")
print(b)