class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(arr)-1
        
        while left+1<right:
            mid = (left+right)//2
            #0<=left<mid<right<=len(arr)
            if arr[mid]<x:
                left = mid
            else:
                right = mid
        
        ans = []
        cnt = 0
        #print(arr[left],arr[right])
        while left>0 and arr[left]>= x:
            if arr[left] == x:
                ans.append(x)
                cnt += 1
                if cnt == k :
                    return ans
            left -= 1
        while right<len(arr) and arr[right]<=x:
            if arr[right] == x:
                ans.append(x)
                cnt += 1
                if cnt == k:
                    return ans
            right += 1
        #print(arr[left],arr[right],ans)
        ## stop at left ==0 or arr[left+1] == x
        ## stop at right == len(arr)-1 or arr[right-1]==x
        
        i = 0
        while True:
            while left >= 0 and cnt<k and arr[left] == x-i:
                ans.insert(0,arr[left])
                cnt += 1
                left -= 1
            while right < len(arr) and cnt<k and arr[right] == x+i:
                ans.append(arr[right])
                cnt += 1
                right += 1
            if cnt == k:
                return ans
            i+=1
        
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        sorted_arr = sorted(arr, key=lambda n: [abs(n-x)])
        
        return sorted(sorted_arr[:k])