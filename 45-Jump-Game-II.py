class Solution:
    def jump(self, nums: List[int]) -> int:
        #核心思想：朝前看两步
        cur_end, cur_farthest, step = 0,0,0
        for i in range(len(nums)-1):
            cur_farthest = max(cur_farthest, i+nums[i])
            if cur_farthest >= len(nums) - 1:
                step += 1
                return step
            if i == cur_end:
                cur_end = cur_farthest
                step += 1
        return step
        
