class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # res = 0
        # for j in range(len(arr1)):
        #     for i in range(j):
        #         res = max(res, abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j))
        # return res
        # #just removing all the abs and you will see. simple math
        l1,l2,l3,l4 = [], [], [], []
        for i in range(len(arr1)):
            l1.append(arr1[i]-arr2[i]+i)
            l2.append(arr1[i]+arr2[i]+i)
            l3.append(-arr1[i]+arr2[i]+i)
            l4.append(-arr1[i]-arr2[i]+i)
        res = []
        res.append(max(l1)-min(l1))
        res.append(max(l2)-min(l2))
        res.append(max(l3)-min(l3))
        res.append(max(l4)-min(l4))
        return max(res)
        
