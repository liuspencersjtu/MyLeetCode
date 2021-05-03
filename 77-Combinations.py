class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 组合的递推公式
        if k==0 or k==n:
            return [[_ for _ in range(1, k+1)]]
        res = self.combine(n-1, k-1)
        res = list(map(lambda x: [n]+x, res))
        res += self.combine(n-1, k)
        return res
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(cur_nums, idx):
            if len(cur_nums) == k:
                res.append(cur_nums)
                return
            if idx == n+1:
                return
            dfs(cur_nums+[idx], idx+1)
            dfs(cur_nums, idx+1)
        res = []
        dfs([], 1)
        return res

