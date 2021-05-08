class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从nums1的尾巴（0的位置）开始修改，这样即使修改到有数据的位置时，
        # 这个数据也已经被使用过了（the place is already dirty）
        # 所以我们可以放心的占用这个位置
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n!=0:
            nums1[:n] = nums2[:n]
