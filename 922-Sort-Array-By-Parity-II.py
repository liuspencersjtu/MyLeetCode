class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for i in range(len(A)):
            if i%2==0:
                if A[i]%2==1:
                    if even:
                        temp = A[i]
                        k = even.pop()
                        A[i] = A[k]
                        A[k] = temp
                    else:
                        odd.append(i)
            if i%2==1:
                if A[i]%2==0:
                    if odd:
                        temp = A[i]
                        k = odd.pop()
                        A[i] = A[k]
                        A[k] = temp
                    else:
                        even.append(i)
        return A
            