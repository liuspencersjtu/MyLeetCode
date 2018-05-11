class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)-1
        while left<right:
            mid = (left+right)//2
            #0<=left<=mid<right<=len(letters)-1
            if letters[mid]<=target and letters[mid+1]>target:
                return letters[mid+1]
            if letters[mid+1]<=target:
                left = mid + 1
            if letters[mid]>target:
                right = mid
        
        #postprocessing
        #right = left
        return letters[0]