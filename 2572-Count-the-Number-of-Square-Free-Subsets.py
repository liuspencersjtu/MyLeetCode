class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
#         # gcd + dp
#         mod = 10**9+7
#         candidates = list(range(2, 31))
#         candidates = [it for it in candidates if it not in [4,9,16,25,8,12,20,24,28,18,27]]
#         from collections import Counter
#         import math
#         cnt = Counter(nums)
#         def helper(candidates):
#             if not candidates:
#                 return 1
#             new_candidates = []
#             for it in candidates[1:]:
#                 if math.gcd(candidates[0], it)==1:
#                     new_candidates.append(it)
                    
            
#             return (cnt[candidates[0]] *helper(new_candidates) + helper(candidates[1:]) )%mod
#         return ((1<<cnt[1])*helper(candidates)-1) % mod

        # bit mask
        mod = 10**9+7
        primes = [2,3,5,7,11,13,17,19,23,29] # the max possible combinations will be 2^(10), 10 = len(primes)
        # from collections import defaultdict
        cnt = [0]*(2**len(primes))
        # when none of the prime is selected, the mask is 0, which indicate the num is 1
        cnt[0] = 1 #consider this for empty subset
        def get_bitmask(n):
            mask = 0
            for i,p in enumerate(primes):
                if n % (p*p)== 0:
                    return -1
                elif n % p == 0:
                    mask |= 1<<i
            return mask
        for num in nums:
            mask = get_bitmask(num)
            if mask<0:
                continue
            for n in range(2**len(primes)):
                if mask&n == 0:
                    cnt[mask|n] += cnt[n]%(mod)
        return (sum(cnt)-1) %mod
                    
