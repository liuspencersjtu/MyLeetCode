class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        a=list([p1,p2,p3,p4])
        a.sort()
        p1,p2,p3,p4=a
        a=(p1[0]-p3[0])==(p2[0]-p4[0])
        b=((p1[1]-p3[1])==(p2[1]-p4[1]))
        c=p1!=p3
        if p2[1]<p3[1]:
            p2,p3=p3,p2
        d=(p1[0]-p3[0])==(p1[1]-p2[1])
        e=((p2[0]-p1[0])*(p3[0]-p1[0])+(p2[1]-p1[1])*(p3[1]-p1[1]))==0
        #print(a,b,c,d,p1,p2,p3,p4)
        return a and b and c and d and e

class Solution2:
    '''
    Use list.sort(key=lambda x:x[0]) instead of list.sort, the later one will use the second column for sorting is the the first column is the same
    '''
    def validSquare(self, p1, p2, p3, p4):
        if p1 == p2 or p2 == p3 or p3 == p4 or p4 == p1:
            return False
        x = [] 
        x.extend((p1, p2, p3, p4))
        x = sorted(x,key=lambda x:x[0])
        x = sorted(x,key=lambda x:x[1], reverse = True)
        p3 = x.pop()
        p4 = x.pop()
        p2 = x.pop()
        p1 = x.pop()
        return (math.sqrt((p1[0]-p3[0])**2 + (p1[1] - p3[1])**2) == math.sqrt((p2[0]-p4[0])**2 + (p2[1] - p4[1])**2)) and ( ( math.sqrt((p1[0]-p4[0])**2 + (p1[1] - p4[1])**2) == math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2) ) and ( math.sqrt((p3[0]-p4[0])**2 + (p3[1] - p4[1])**2) == math.sqrt((p3[0]-p2[0])**2 + (p3[1] - p2[1])**2) ) )

## 其实对于这道题来说，只要check对角线相等且垂直平分就好了。
class Solution3:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        a=list([p1,p2,p3,p4])
        a.sort()
        p1,p2,p3,p4=a
        c1=[p4[0]-p1[0],p4[1]-p1[1]]
        c2=[p3[0]-p2[0],p3[1]-p2[1]]
        d1=(c1[0]*c2[0]+c1[1]*c2[1])==0
        d2=(c1[0]*c1[0]+c1[1]*c1[1])==(c2[0]*c2[0]+c2[1]*c2[1])
        d3=p1!=p2
        d4=(p3[0]+p2[0])==(p1[0]+p4[0])
        return d1 and d2 and d3 and d4