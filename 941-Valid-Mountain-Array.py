class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n<3:
            return False
        # 0 represent ascending
        mark = 0
        if A[0]>A[1]:
            return False
        k = 1
        while k<n:
            if A[k]>A[k-1]:
                if mark>0:
                    return False
                k+=1
            elif A[k]<A[k-1]:
                if A[k-2]<A[k-1]:
                    k+=1
                    mark+=1
                    # not necessary
                    #if mark>1:
                    #    return False
                else:
                    k+=1
            else:
                return False
        if mark == 1:
            return True
        else:
            return False
                