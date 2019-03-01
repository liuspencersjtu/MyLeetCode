class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        while n>1:
            ans = self.helper(ans)
            n-=1
        return ans
    def helper(self,n):
        p = 1
        cnt = 1
        res = ""
        if len(n)==1:
            return '11'
        #for i in range(1,len(n)):
        N = len(n)
        while p<N:
            if n[p]!=n[p-1]:
                res+=str(cnt)+n[p-1]
                cnt=1
            else:
                cnt+=1
            p+=1
        res+=str(cnt)+n[-1]
        return res
