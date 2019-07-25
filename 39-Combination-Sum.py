class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def helper(target,cmb,k):
            if target == 0:
                res.add(tuple(cmb))
            elif target<0:
                return
            for i in range(k,len(candidates)):
                helper(target-candidates[i],cmb+[candidates[i]],i)
        helper(target,[],0)
        return list(res)
