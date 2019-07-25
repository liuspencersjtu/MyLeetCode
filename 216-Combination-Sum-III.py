class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cmb = []
        def helper(target,j,cmb):
            if target == 0 and len(cmb)==k:
                res.append(cmb.copy())
            elif target<0 or len(cmb)==k or j>9:
                return
            for i in range(j,10):
                #choose
                cmb=cmb+[i]
                #recursive
                helper(target-i,i+1,cmb)
                #unchoose
                cmb.pop()
        helper(n,1,cmb)
        return res
