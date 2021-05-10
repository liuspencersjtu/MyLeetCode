class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 选或者不选，二叉决策问题，用dfs
        memo = set()
        nums.sort()
        N = len(nums)
        def dfs(path, i):
            if i == N:
                memo.add(tuple(path))
                return
            else:
                dfs(path+[nums[i]], i+1)
                dfs(path, i+1)
        dfs([], 0)
        return [list(_) for _ in memo]
        
