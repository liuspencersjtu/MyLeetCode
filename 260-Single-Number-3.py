class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        table = {}
        for item in nums:
            if not table.get(item):
                table[item] = 1
            else:
                table[item] = 0
        newNums = []
        for item in table.keys():
            if table[item] == 1:
                newNums += [item]
        return newNums
                  