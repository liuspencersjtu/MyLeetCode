class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
	# backtracing of bfs with pruning
        self.res = []
        def dfs(num):
            if len(num) == N:
                self.res.append(int(''.join([str(_) for _ in num])))
                return 
            num1 = num[-1]
            num2 = num1+K
            if num2<10:
                dfs(num+[num2])
            if K!=0:
                num3 = num1-K
                if num3>=0:
                    dfs(num+[num3])
            return
        if N>1:
            for p in range(1,10):
                dfs([p])
        else:
            for p in range(10):
                dfs([p])
        return self.res
        
                
