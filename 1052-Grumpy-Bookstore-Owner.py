class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = 0
        if len(customers)<=X:
            return sum(customers)
        for i in range(len(customers)):
            if grumpy[i]==0:
                res += customers[i]
        wdsum = 0
        for i in range(X):
            wdsum += customers[i]*grumpy[i]
        wdbeginning = customers[0] if grumpy[0]==1 else 0
        temp = res+wdsum
        #print(res,wdsum, wdbeginning)
        for i in range(X,len(customers)):
            #if grumpy[i]==1:
            wdsum += (customers[i]*grumpy[i]-wdbeginning)
            wdbeginning = customers[i-X+1] *grumpy[i-X+1]             
            temp = max(temp, res+wdsum)
        res = temp
        return res
