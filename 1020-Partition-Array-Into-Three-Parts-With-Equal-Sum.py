class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        B = []
        prefix_sum = 0
        for it in A:
            prefix_sum += it
            B.append(prefix_sum)
        #print(B)
        total = B[-1]
        if total%3 != 0:
            return False
        div1, div2 = total//3, total//3*2
        if div1 in B:
            k=B.index(div1)
            if div2 in B[k+1:]:
                return True
            else:
                return False
        else:
            return False
