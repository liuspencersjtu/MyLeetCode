class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left=[]
        max_right=[]
        N=len(height)
        left = 0
        right = 0
        for i in range(N):
            left = max(left,height[i])
            max_left.append(left)
        for i in range(N-1,-1,-1):
            right = max(right,height[i])
            max_right.insert(0,right)
        ans = 0
        for i in range(N):
            ans += min(max_left[i],max_right[i])-height[i]
        return ans
        
        '''
        #brute force
        ans = 0
        N=len(height)
        for i in range(N):
            max_left,max_right = 0,0
            for j in range(i,-1,-1):
                max_left=max(max_left,height[j])
            for j in range(i,N):
                max_right=max(max_right,height[j])
            ans+=min(max_left,max_right)-height[i]
        return ans
        '''
