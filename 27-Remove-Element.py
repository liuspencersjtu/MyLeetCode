class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast,slow = 0, 0
        N = len(nums)
        while fast<N:
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow
