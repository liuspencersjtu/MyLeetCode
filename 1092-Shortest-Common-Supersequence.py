from functools import lru_cache
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # this will cause a memory exceed
        #memo = {}
        @lru_cache(1000000)
        def dp(i,j):
            #if (i,j) in memo:
            #    return memo[(i,j)]
            if i == -1 and j ==-1:
                return '', 3
            elif i == -1:
                return str2[:j+1], 2
            elif j == -1:
                return str1[:i+1], 1
            s1, last1 = dp(i-1,j)
            s2, last2 = dp(i,j-1)
            if last1 == 2 and s1[-1] == str1[i]:
                last1 = 3
            else:
                s1 = s1+str1[i]
                last1 = 1
            if last2 == 1 and s2[-1] == str2[j]:
                last2 = 3
            else:
                s2 = s2+str2[j]
                last2 = 2
            if len(s1)<=len(s2):
                #memo[(i,j)] = (s1, last1)
                return s1, last1
            else:
                #memo[(i,j)] = (s2, last2)
                return s2, last2
        res, _ = dp(len(str1)-1,len(str2)-1)
        return res
