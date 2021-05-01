class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 摩尔排序
        if len(nums)==1:
            return nums
        candidate1 = nums[0]
        vote1, vote2 = 0, 0
        # 假设存在某个数i不是现在的candidate但是数量超过三分之一，
        # 那么必然两个candidate之后至少有一个要被消耗到0然后换掉，
        # 否则我们会推出一个悖论，即存在3个数出现都超过三分之一次
        for num in nums:
            if num != candidate1:
                candidate2 = num
                break
        for num in nums:
            if candidate1 == num:
                vote1 +=1
                continue
            elif candidate2 == num:
                vote2 += 1
                continue
            if vote1 == 0:
                candidate1 = num
                vote1 = 1
                continue
            elif vote2 == 0:
                candidate2 = num
                vote2 = 1
                continue
            vote1 -= 1
            vote2 -= 1
        vote1, vote2 = 0, 0
        for num in nums:
            if num == candidate1:
                vote1 += 1
            elif num == candidate2:
                vote2 += 1
        res = []
        if vote1>len(nums)//3:
            res.append(candidate1)
        if vote2>len(nums)//3:
            res.append(candidate2)
        return res
            
                    
