'''
backtracking
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, curr_total, index, curr):
            ##
            if curr_total <0:
                return
            elif curr_total==0:
                res.append(list(curr))
                return
            else:
                for i in range(index,len(candidates)):
                    if i>index and candidates[i]==candidates[i-1]:
                        continue
                    curr.append(candidates[i])
                    dfs(candidates, curr_total-candidates[i], i+1, curr)
                    curr.pop()
        
        res = []
        candidates.sort()
        if not candidates:
            return []
        dfs(candidates, target, 0, [])
        return res
