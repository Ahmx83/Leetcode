class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: list[list[int]]
        :rtype: int
        """
        if len(accounts) == 1:
            return sum(accounts[0])
        return sum(max(*accounts, key=lambda x: sum(x)))

