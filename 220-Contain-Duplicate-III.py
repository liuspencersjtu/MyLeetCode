class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 这里利用了一个bucket的思想讲nums中的元素都处以t
        # 这样就不用在lookup中对[num-t,num+t]区间内的值都进行存储
        from collections import defaultdict
        lookup = defaultdict(int)
        if t == 0:
            for i, num in enumerate(nums):
                if num in lookup and i - lookup[num]<=k:
                    return True
                lookup[num] = i
            return False
        for i, num in enumerate(nums):
            if num//t in lookup:
                if i - lookup[num//t]<=k and abs(nums[lookup[num//t]]-num)<=t:
                    return True
            if num//t+1 in lookup:
                if i - lookup[num//t+1]<=k and abs(nums[lookup[num//t+1]]-num)<=t:
                    return True
            if num//t-1 in lookup:
                if i - lookup[num//t-1]<=k and abs(nums[lookup[num//t-1]]-num)<=t:
                    return True
            lookup[num//t] = i
        return False
