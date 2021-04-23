class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 首先要看明白只需要和前面的数字比而不需要和后面的数字比，这样能第一步简化问题
        if len(nums)<=k:
            return not len(set(nums))==len(nums)
        if len(set(nums[:k])) != k:
            return True
        
        lookup = {}                
        for i, num in enumerate(nums):
            if i>=k and num in lookup and i-lookup[num]<=k:
                return True
            else:
                lookup[num] = i
        return False
        
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 这样也能过，但是太慢了，应该用字典，类似two sum
        if len(nums)<=k:
            return not len(set(nums))==len(nums)
        if len(set(nums[:k])) != k:
            return True
        for i in range(k,len(nums)):
            if nums[i] in nums[i-k:i]:
                return True
        return False

