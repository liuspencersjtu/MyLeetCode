class Solution:
    # 这里唯一需要注意的就是python里对字符串切片a[i,j]里不包括a[j]
    # a[0:0] = '',只有a[0:1] == a[0]
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    cnt += 1
        
        return cnt