class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        def rotate(s):
            return s[1:]+s[0]
        
        if A == B:
            return True
        for i in range(len(A)):
            if A == B:
                return True
            A = rotate(A)
            
        return False