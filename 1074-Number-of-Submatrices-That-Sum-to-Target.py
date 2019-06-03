import copy
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for line in matrix:
            for i in range(1,len(line)):
                line[i]=line[i-1]+line[i]
                
        res = 0
        for i in range(len(matrix[0])):
            for j in range(i,len(matrix[0])):
                memo = collections.defaultdict(int)
                memo[0]=1
                prefixsum = 0
                for k in range(len(matrix)):
                    prefixsum += matrix[k][j]- (matrix[k][i-1] if i>0 else 0)
                    res += memo[prefixsum-target]
                    memo[prefixsum]+=1
        return res
