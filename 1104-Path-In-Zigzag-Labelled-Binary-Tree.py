import math
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 2^k-1>=label>2^(k-1)-1
        #log2(label+1)+1>k>=log2(label+1)
        level = math.ceil(math.log2(label+1))
        res = []
        #if level%2==1:
        order = label - (2**(level-1)-1)
        #else:
        #    order = level - (label - (2^(level-1)-1))
        #print(order,level,2**(level-1)-1)
        while level>0:
            #print(order,level,2**(level-1)-1)
            res.append(2**(level-1)-1+order)
            level -= 1
            order = 2**(level-1) - math.ceil(order/2) + 1
        return res[::-1]
