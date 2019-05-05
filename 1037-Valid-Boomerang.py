import math
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a,b,c=points
        dotproduct = ((b[0]-a[0])*(c[0]-a[0])+(b[1]-a[1])*(c[1]-a[1]))
        product = math.sqrt(((b[0]-a[0])**2+(b[1]-a[1])**2)*((c[0]-a[0])**2+(c[1]-a[1])**2))
        if product!=0 and abs(float(dotproduct))!=float(product):
            return True
        return False
