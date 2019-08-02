from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # cheat
        # perm = permutations(nums,len(nums))
        # return list(set(perm))
        
        ans = []
        nums = sorted(nums)
        def finding_ans(array, temp):
            if len(array) == 1:
                ans.append(temp+array)
                return
            for i in range(len(array)):
                if i > 0 and array[i] == array[i-1]:
                    continue
                finding_ans(array[:i] + array[i+1:], temp + [array[i]])
        finding_ans(nums, [])
        return ans
        
        # if len(nums) == 0:
        #     return []
        # if len(nums) == 1:
        #     return [nums]
        # res = []
        # for i in range(len(nums)):
        #     prefix = nums[i]
        #     rest = nums[:i] + nums[i+1:]
        #     for j in self.permuteUnique(rest):
        #         if [prefix]+j not in res:
        #             res.append([prefix]+j)
        # return res
