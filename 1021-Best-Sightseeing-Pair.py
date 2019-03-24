class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        leftbiggest = []
        rightbiggest = []
        temp = 0
        for i in range(len(A)):
            temp = max(temp, A[i]+i)
            leftbiggest.append(temp)
        temp = -float('inf')
        for i in range(len(A)-1,-1,-1):
            ##
            temp = max(temp,A[i]-i)
            rightbiggest.insert(0,temp)
        rightbiggest.pop(0)
        res = 0
        #print(leftbiggest,rightbiggest)
        #left, right = 0, 0
        for i in range(len(A)-1):
            ##
            res = max(res, leftbiggest[i]+rightbiggest[i])
        return res
