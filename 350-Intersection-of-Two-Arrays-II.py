class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        store = {}
        res = []
        for i in nums1:
            store[i]=store.get(i,0)+1
        for i in nums2:
            if store.get(i,0) != 0:
                res.append(i)
                store[i] = store[i] - 1
        return res