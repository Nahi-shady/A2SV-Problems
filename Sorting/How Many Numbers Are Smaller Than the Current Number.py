class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        val = []
        for i in nums:
            sum = [k for k in nums if k < i]
            val.append(len(sum))
        return val