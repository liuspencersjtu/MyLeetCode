class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # https://leetcode.com/problems/rearranging-fruits/solutions/3143917/java-c-python-two-ways-to-swap/
        from collections import Counter
        cnt = Counter(basket1+basket2)
        for k in cnt:
            if cnt[k]%2==1:
                return -1
            else:
                cnt[k] >>=1 # cnt[k]= cnt[k]//2
        A = cnt.elements() # A += [k]*cnt[k] for k in cnt
        delta1 = list((Counter(basket1)-cnt).elements())
        delta2 = list((Counter(basket2)-cnt).elements())
        cnt_delta = Counter(delta1+delta2)
        # for k in cnt_delta:
        #     cnt_delta[k] >>=1
        B = list(cnt_delta.elements())
        B.sort()
        a_min = min(A)
        res = 0
        print(delta1, delta2)
        for i in range(len(delta1)):
            res += min(2*a_min, B[i])
        return res
            
        
        
                
