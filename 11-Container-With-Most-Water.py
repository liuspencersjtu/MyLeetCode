class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0,len(height)-1
        maxarea=abs((j-i)*min(height[j],height[i]))
        while j>i:
            temp=abs((j-i)*min(height[j],height[i]))
            if temp>maxarea:
                maxarea=temp
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maxarea
                