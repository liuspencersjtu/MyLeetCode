class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        tmp = [0]*N
        low, fast = 0, 0
        while fast < N:
            if arr[low] == 0:
                fast+=2
                low+=1
            else:
                tmp[fast]=arr[low]
                fast +=1
                low +=1
        for i in range(N):
            arr[i] = tmp[i]
            
            
