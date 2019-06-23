# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binarySearch (arr, l, r, x): 
            if r >= l: 
                mid = int(l + (r - l)//2)
                mid_val = arr.get(mid)
                if mid_val == x: 
                    return mid 
                elif mid_val > x: 
                    return binarySearch(arr, l, mid-1, x) 
                else: 
                    return binarySearch(arr, mid+1, r, x) 
            else: 
                return float('inf')
        def helper(arr, l, r, target):
            if r-l<=1:
                return float('inf')
            mid = (l+r)//2
            mid_val = arr.get(mid)
            midplus1_val = arr.get(mid+1)
            up = midplus1_val>mid_val
            if mid_val == target and up == True:
                return mid
            elif mid_val == target and up == False:
                tmp = helper(arr, l, mid, target)
                return min(tmp, mid)
            elif mid_val > target and up == True:
                left = binarySearch(arr, l, mid, target)
                right = helper(arr, mid, r, target)
                return min(left, right)
            elif mid_val > target and up == False:
                left = helper(arr, l, mid, target)
                right = binarySearch(arr, mid, r, target)
                return min(left, right)
            elif mid_val < target and up == True:
                right = helper(arr, mid, r, target)
                return right
            elif mid_val < target and up == False:
                left = helper(arr, l, mid, target)
                return left
            print('no way', mid_val, mid, l, r, target, up)
        res = helper(mountain_arr, 0 , mountain_arr.length()-1, target)
        head = mountain_arr.get(0)
        if head == target:
            return 0
        if res == float('inf'):
            tail = mountain_arr.get(mountain_arr.length()-1)
            if tail == target:
                return mountain_arr.length()-1
            return -1
        else:
            return res
        
