class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        brackets = list(s)
        d = {'(': ')', '[': ']', '{': '}'}
        open_brackets = d.keys()
        close_brackets = d.values()

        opened = []
        for brack in brackets:
            if brack in open_brackets:
                opened.append(brack)
            elif brack in close_brackets:
                if not opened:
                    return False
                if d[opened[-1]] != brack:
                    return False
                opened.pop()
        return not opened


sol = Solution().isValid
a = sol("()")
print(a)
b = sol("){")
print(b)