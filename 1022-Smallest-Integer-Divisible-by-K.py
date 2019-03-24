class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0:
            return -1
        cnt = 1
        num = 1
        memo = set()
        a = 0
        while not a in memo:
            memo.add(a)
            a = num%K
            if a == 0:
                return cnt
            cnt+=1
            num=num*10+1
        return -1
