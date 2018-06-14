class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        xlist = [A,E,C,G]
        xlist.sort()
        ylist = [F,B,H,D]
        ylist.sort()
        rectangles = [(A,B,C,D),(E,F,G,H)]
        area = 0
        for i in range(len(xlist)-1):
            for j in range(len(ylist)-1):
                tag = 0
                for (x1,y1,x2,y2) in rectangles:
                    if xlist[i]>=x1 and xlist[i+1]<=x2 and ylist[j]>=y1 and ylist[j+1]<=y2:
                        tag = 1
                        break
                if tag == 1:
                    area += (xlist[i+1]-xlist[i])*(ylist[j+1]-ylist[j])
        return area