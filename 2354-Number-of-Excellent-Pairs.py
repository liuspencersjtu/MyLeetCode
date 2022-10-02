class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        hamming = [self.hammingWeight(num) for num in set(nums)]
        hamming.sort()
        ans = 0
        for h in hamming:
            ans += len(hamming) - bisect.bisect_left(hamming, k - h)
        return ans
        
    def hammingWeight(self, n):
        ans = 0
        while n:
            n &= (n - 1)
            ans += 1
        return ans

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # inclusion-exclusion principle
        # https://leetcode.com/problems/number-of-excellent-pairs/discuss/2324984/JavaC%2B%2BPython-Inclusion-Exclusion-Principle
        from collections import defaultdict
        cnt = defaultdict(int)
        nums = list(set(nums))
        def count_bits(num):
            cnt = 0
            while num:
                num &= (num-1)
                cnt += 1
            return cnt
        for num in nums:
            cnt[count_bits(num)] += 1
        res = 0
        for i in cnt.keys():
            for j in cnt.keys():
                if i+j >= k:
                    res += cnt[i]*cnt[j]
        return res
