class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l, r = 0, len(nums)-1
        cur = float('inf')
        N = len(nums)
        res = 0
        for i in range(N):
            l,r = i+1,N-1
            while l<r:
                #print(i,l,r,cur)
                tmp = nums[l]+nums[i]+nums[r]
                if tmp==target:
                    return target
                elif tmp>target:
                    #cur = min(cur, abs(tmp-target))
                    if cur > abs(tmp-target):
                        cur = abs(tmp-target)
                        res = tmp
                    r-=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                else:
                    # tmp<target
                    #cur = min(cur, abs(tmp-target))
                    if cur > abs(tmp-target):
                        cur = abs(tmp-target)
                        res = tmp
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        #print(i,l,r,cur)
        return res
                    
                
