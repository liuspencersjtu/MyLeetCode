class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        # rank 18%,primitive answer
        # 这里唯一需要注意的就是python里对字符串切片a[i,j]里不包括a[j]
        # a[0:0] = '',只有a[0:1] == a[0]
        cnt = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    cnt += 1
        
        return cnt
        '''
        '''
        # rank 30+% using DP
        n = len(s)
        m = [ [False for _ in range(n)] for _ in range(n)]
        w = 1
        
        #each char is a palindrome
        for i in range(n):
            m[i][i] = True
        
        # if two adjacent chars match, they form a palindrom
        for i in range(n-w):
            m[i][i+w] = s[i]==s[i+w]
        
        # for 'abxba' to be a palindrome, inner strings 'bxb' should also be a plaindrom and last chars a,a should match
        for w in range(2,n):
            for i in range(n-w):
                m[i][i+w] = m[i+1][i+w-1] and ( s[i] == s[i+w])
        
        count = 0
        ## simply count valid Trues
        for i in range(n):
            for j in range(n):
                if m[i][j]:
                    count+=1
        return count
        '''
        # rank 66% using DP, this key is find a center(like 'bab', the center is a and 'baab', the center is 'aa')
        # then try to expand the substrings, if the outside front and end do not equal, then stop expanding 
        length = len(s)
        res = 0

        for i in range(length):
            res += (self.check(i,i,s) + self.check(i,i+1,s))
        return res

    def check(self,x,y,s):
        count = 0
        while x >= 0 and y < len(s):
            if s[x] != s[y]:
                return count
            else:
                count+=1
            x-=1
            y+=1
        return count