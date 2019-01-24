class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return res.values()
