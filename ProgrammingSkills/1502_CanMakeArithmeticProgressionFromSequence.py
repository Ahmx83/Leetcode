class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: list[int]
        :rtype: bool
        """
        arr.sort()
        DIFF = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != DIFF:
                return False
        return True