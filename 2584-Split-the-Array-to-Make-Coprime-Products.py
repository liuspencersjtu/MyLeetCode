class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        hashmap = {}
        import math
        def get_primes(num : int) -> List[int]:
            res = []
            p = 2
            while p*p<=num:
                if num%p == 0:
                    res.append(p)
                while num%p == 0:
                    num = num//p
                p += 1
            if num%2 == 1:
                res.append(num)
            return res

        primes = []
        for i, num in enumerate(nums):
            primes.append(get_primes(num))
            for x in primes[i]:
                hashmap[x]=i
        lmax = 0
        # print(primes)
        # print(hashmap)
        for i in range(len(primes)-1):
            for x in primes[i]:
                lmax = max(lmax, hashmap[x])
            if lmax==i:
                return i
        return -1
                
        
            
            
