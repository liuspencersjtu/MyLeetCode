class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 第一眼想想应该可以BFS，但是实际上应该是dp。BFS会超时
        M, N, K = len(s1), len(s2), len(s3)
        if M + N != K:
            return False
        from functools import lru_cache
        @lru_cache(256)
        def helper(i,j):
            if i == M and j == N:
                return True
            res = False
            if i < M and s1[i] == s3[i+j]:
                res |= helper(i+1, j)
            if j < N and s2[j] == s3[i+j]:
                res |= helper(i, j+1)
            return res
        return helper(0,0)
    
        # 上面是反着来，也可以正着来dp
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, len(s2)+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else: # 前面都不符合了，后面肯定不符合了
                break
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True
        return dp[-1][-1]
        
        
        
        
        
        
        
        candidates = [(0,0,0)]
        M, N, K = len(s1), len(s2), len(s3)
        if K != M+N:
            return False
        # BFS
        while candidates:
            new_candidates = []
            for i, (p1, p2, p3) in enumerate(candidates):
                while p1<M and s1[p1] == s3[p3]:
                    p1 += 1
                    p3 += 1
                if p3 == K:
                    return True
                elif p1 != candidates[i][0]:
                    new_candidates.append([p1-1, p2, p3-1])
                p3 = candidates[i][2]
                while p2<N and s2[p2] == s3[p3]:
                    p2 += 1
                    p3 += 1
                if p3 == K:
                    return True
                elif p2 != candidates[i][1]:
                    new_candidates.append([p1, p2-1, p3-1])
            if not new_candidates:
                return False
            else:
                candidates = new_candidates
        return False
