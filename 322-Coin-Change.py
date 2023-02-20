class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        from functools import lru_cache

        @lru_cache(10**4)
        def dfs(amount):
            if amount==0:
                return 0
            if amount<0:
                return -1
            mincost = float('inf')
            for coin in coins:
                ret = dfs(amount-coin)
                if ret>=0:
                    mincost = min(mincost, ret+1)
            return mincost if mincost != float('inf') else -1
        
        return dfs(amount)
        
            
