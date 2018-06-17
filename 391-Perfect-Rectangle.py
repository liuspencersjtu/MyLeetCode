class Solution:
    # a solution, but will exceed the time limit
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        xlist = [item[0] for item in rectangles] + [item[2] for item in rectangles]
        ylist = [item[1] for item in rectangles] + [item[3] for item in rectangles]
        xlist = list(set(xlist))
        ylist = list(set(ylist))
        xlist.sort()
        ylist.sort()
        print(xlist)
        print(ylist)
        for i in range(len(xlist)-1):
            for j in range(len(ylist)-1):
                dirty = 0
                for x1,y1,x2,y2 in rectangles:
                    if all(
                        [xlist[i]>=x1,
                        xlist[i+1]<=x2,
                        ylist[j]>=y1,
                        ylist[j+1]<=y2]
                    ):
                        if not dirty:
                            dirty = 1
                        else:
                            return False
                if not dirty:
                    return False
        return True
                