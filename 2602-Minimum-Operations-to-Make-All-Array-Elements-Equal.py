class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        presum = [0] + list(accumulate(nums)) # 不加0的话presum[-1]-presum[0]也最多涵盖第一到最后的和
        import bisect
        res = []
        for i,q in enumerate(queries):
            idx = bisect.bisect_left(nums,q)
            tmp = 0
            if idx>0:
                tmp += idx*q-presum[idx]
            if idx<len(nums):
                tmp += presum[len(nums)] - presum[idx] - (len(nums)-idx)*q
            res.append(tmp)
        return res
        
        
        
        # approch 2): TLE error
        # xxxxxx 5 xxxx 12 xxxx
        # ++++++ 0 ---- -- ----
        # ++++++ + ++++ 00 ----
        # +k1*7    recal.  -k2*7
        nums.sort()
        res = []
        if not queries:
            return []
        import bisect
        idx = bisect.bisect_left(nums, queries[0])
        res.append(0)
        for num in nums:
            res[0]+=abs(num-queries[0])
        for i in range(1, len(queries)):
            res.append(res[-1])
            if queries[i]==queries[i-1]:
                continue
            elif queries[i]>queries[i-1]:
                idx = bisect.bisect_left(nums, queries[i-1])
                idx_new = bisect.bisect_right(nums, queries[i])
                res[-1] += (queries[i]-queries[i-1])*idx
                res[-1] -= (queries[i]-queries[i-1])*(len(nums)-idx_new)
                for j in range(idx,idx_new):
                    res[-1] -= abs(nums[j]-queries[i-1])
                    res[-1] += abs(nums[j]-queries[i])
            else:# queries[i]<queries[i-1]
                idx_new = bisect.bisect_left(nums, queries[i])
                idx = bisect.bisect_right(nums, queries[i-1])
                res[-1] -= (queries[i-1]-queries[i])*idx_new
                res[-1] += (queries[i-1]-queries[i])*(len(nums)-idx)
                for j in range(idx_new,idx):
                    res[-1] -= abs(nums[j]-queries[i-1])
                    res[-1] += abs(nums[j]-queries[i])
                idx = idx_new
        return res
